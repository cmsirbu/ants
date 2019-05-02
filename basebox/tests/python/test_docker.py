import docker


def test_docker_networks(device_inventory):
    """
    Test the docker library by checking the default docker networks exist.
    """
    client = docker.from_env()
    networks = [net.name for net in client.networks.list()]

    assert "bridge" in networks
    assert "host" in networks
    assert "none" in networks
