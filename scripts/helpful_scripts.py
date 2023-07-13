from brownie import network, config, accounts, MockV3Aggregator

DECIMALS = 8
# DECIMALS：小数点
STARTING_PRICE = 200000000000

# 将ganache-local定义为需要部署模拟合约的情况
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

# 将mainnet-fork-dev设置为需要生成账户，但不需要部署模拟喂价合约的情况
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]


def get_account():
    # 如果部署到本地链（包括主链分叉）则使用本地的模拟账户，否则使用真实账户
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"正在{network.show_active()}网络中部署模拟喂价合约...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("模拟喂价合约已部署完成！")
