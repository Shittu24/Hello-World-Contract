from brownie import network, config, HelloWorld
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    number = HelloWorld.deploy(
        {"from": account, "gas_limit": 1000000}, 
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    number.store (5, {"from": account})
  
    print(f"Starting value is {number.retrieve()}")
   # number.wait(1)
    print("number has been upgraded!")
    number.increment({"from": account, "gas_limit": 1000000})
    print(f"Ending value is {number.retrieve()}")

