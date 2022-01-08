from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS= ["mainnet-fork", "mainnet-fork-dev"]
DECIMANLS= 18
STARTING_PRICE=2000
LOCAL_DEPLOYMENT_ENVIRONMENTS= ["development","ganache-local"]

def get_account():
    if network.show_active()=="development" or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active} ")
    print("Deploying mocks ...")
    if len(MockV3Aggregator)<=0:
         MockV3Aggregator.deploy(DECIMANLS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
    print("Mocks Deployed")
   