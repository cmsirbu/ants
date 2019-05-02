from jinja2 import Template


def test_jinja2(device_inventory):
    """
    Test the Jinja2 library by generating text from a template.
    """

    test_template = """
    interface Ethernet{{ intf_id }}
     ip address {{ intf_ip }}
    """

    test_result = """
    interface Ethernet1
     ip address 1.2.3.4/24
    """

    template = Template(test_template)
    result = template.render(intf_id=1, intf_ip="1.2.3.4/24")

    assert result == test_result
