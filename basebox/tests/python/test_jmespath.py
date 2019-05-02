import jmespath


def test_jmespath_search(device_inventory):
    """
    Test the jmespath library by querying the inventory.
    """
    juniper_devices = jmespath.search("all.children.juniper.children", device_inventory)

    assert "vQFX" in juniper_devices
    assert len(juniper_devices["vQFX"]) == 1
