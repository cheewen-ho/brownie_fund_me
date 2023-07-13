from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    print(account)

    # 根据部署网络的不同，获取不同的喂价合约地址
    # 如果部署到本地链，则在本地模拟部署一个假的喂价合约并获取其地址
    # 假的喂价合约，或者叫模拟合约一般放在contract->test文件夹中
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
        # publish_source参数控制是否将合约公开发布，如果没有这个参数默认表示不公开
        # .get("verify")也可以写成["verify"]，但是前者更安全，如果我们忘记在config中添加verify，后者会出错而前者会返回false
    )
    print(f"合约已部署到{network.show_active()}网络中，合约地址为{fund_me.address}!")
    return fund_me


def main():
    deploy_fund_me()
