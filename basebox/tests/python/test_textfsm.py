import textfsm, yaml

def test_textfsm_clitable_cisco(device_inventory):
    """
    Test the textfsm library by parsing output from Cisco IOS show ip route
    and comparing to expected output. Test data taken from ntc-templates repo.
    """

    re_table = textfsm.TextFSM(open("files/cisco_ios_show_ip_route.template"))

    with open("files/cisco_ios_show_ip_route.raw") as f:
        raw_text_data = f.read()

    data = re_table.ParseText(raw_text_data)
    data_headers = [h.lower() for h in re_table.header]

    parsed_result = []

    for line in data:
        parsed_result.append(dict(zip(data_headers, line)))

    with open("files/cisco_ios_show_ip_route.parsed") as f:
        reference_result = yaml.load(f, Loader=yaml.FullLoader)

    for i in range(len(parsed_result)):
        assert parsed_result[i] == reference_result[i]
