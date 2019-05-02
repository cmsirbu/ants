import pytest
import yaml


@pytest.fixture(scope="session")
def device_inventory():
    """
    Load the device inventory and provide it to all tests.
    """
    with open("inventory.yml", "r") as inv_file:
        inv = yaml.load(inv_file, Loader=yaml.FullLoader)

    assert type(inv) == dict

    return inv
