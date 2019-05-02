from json import loads
from subprocess import run, PIPE
from os import environ


def test_junos_facts():
    """
    Test the ansible junos netconf modules.
    """

    ansible_env = environ.copy()
    ansible_env["ANSIBLE_STDOUT_CALLBACK"] = "json"

    command = ["ansible-playbook", "ansible/junos.yml"]
    process_result = run(command, stdout=PIPE, stderr=PIPE, env=ansible_env)
    playbook_result = loads(process_result.stdout.decode("utf-8"))

    assert process_result.returncode == 0

    for host, result in playbook_result["stats"].items():
        assert result["ok"] == 2
        assert result["failures"] == 0
