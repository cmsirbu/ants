from netaddr import IPAddress, IPNetwork


def test_netaddr(device_inventory):
    """
    Test the netaddr library by doing IPv4/6 subnetting math.
    """

    assert IPAddress("192.0.2.1").version == 4
    assert IPNetwork("192.0.2.0/24").ip == IPAddress("192.0.2.0")
    assert IPNetwork("192.0.2.0/24").size == 256

    assert (
        str(IPNetwork("2001:0DB8:0000:CD30:0000:0000:0000:0000/60"))
        == "2001:db8:0:cd30::/60"
    )
    assert str(IPNetwork("2001:0DB8::CD30:0:0:0:0/60")) == "2001:db8:0:cd30::/60"
    assert str(IPNetwork("2001:0DB8:0:CD30::/60")) == "2001:db8:0:cd30::/60"
