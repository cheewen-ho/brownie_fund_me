from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"目前的最低捐助额是{entrance_fee}wei")
    print("捐助中...")
    # 捐助最低捐助额
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f"已捐助{entrance_fee}wei")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
