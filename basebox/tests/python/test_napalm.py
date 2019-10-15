from napalm import get_network_driver


def test_napalm_eos_facts(device_inventory):
    """
    Test the napalm library by gathering facts and ntp config from vEOS.
    """

    devices = device_inventory["all"]["children"]["arista"]["children"]["vEOS"]["hosts"]

    driver_eos = get_network_driver("eos")

    for host in devices:
        veos = driver_eos(
            devices[host]["ansible_host"],
            devices[host]["ansible_user"],
            devices[host]["ansible_password"],
        )

        veos.open()

        facts = veos.get_facts()

        assert devices[host]["version"] in facts["os_version"]
        assert facts["vendor"] == "Arista"
        assert facts["model"] == devices[host]["model"]

        # Dependency test: Textfsm is used to parse output.
        ntp_servers = veos.get_ntp_servers()

        assert ntp_servers == {"100.100.100.200": {}}

        veos.close()
