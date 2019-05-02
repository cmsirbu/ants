from lxml import etree
from jnpr.junos import Device


def test_pyez_facts(device_inventory):
    """
    Test the pyEZ library by connecting to a vQFX device and fetching facts.
    """
    devs = device_inventory["all"]["children"]["juniper"]["children"]["vQFX"]["hosts"]

    for dev_name, dev_data in devs.items():
        print(f"Testing {dev_name} with {dev_data}.")

        with Device(
            host=dev_data["ansible_host"],
            user=dev_data["ansible_user"],
            ssh_private_key_file=device_inventory["all"]["vars"][
                "ansible_ssh_private_key_file"
            ],
        ) as dev:

            assert dev.facts["model"] == dev_data["model"]
            assert dev.facts["version"] == dev_data["version"]


def test_pyez_xml_config(device_inventory):
    """
    Test pyEZ+lxml by fetching the configuration from a vQFX device.
    """
    devs = device_inventory["all"]["children"]["juniper"]["children"]["vQFX"]["hosts"]

    for dev_name, dev_data in devs.items():
        print(f"Testing {dev_name} with {dev_data}.")

        with Device(
            host=dev_data["ansible_host"],
            user=dev_data["ansible_user"],
            ssh_private_key_file=device_inventory["all"]["vars"][
                "ansible_ssh_private_key_file"
            ],
        ) as dev:

            config = dev.rpc.get_config(options={"format": "text"})
            assert len(etree.tostring(config)) >= 50
