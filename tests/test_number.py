from brownie import network, config, HelloWorld
from scripts.helpful_scripts import get_account


def test_number():
    account = get_account()
    number = HelloWorld.deploy(
        {"from": account, "gas_limit": 1000000},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    assert number.retrieve() == 6
    number.increment({"from": account, "gas_limit": 1000000})
    assert number.retrieve() == 10
