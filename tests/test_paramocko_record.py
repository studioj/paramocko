import unittest
from unittest.mock import MagicMock

from paramocko import SSHClient
from paramiko import SSHClient as paramikoSSHClient


class TestSSHClientRecord(unittest.TestCase):
    def testSSHClient_is_the_same_type_than_paramiko_ssh_client(self):
        paramocko_client = SSHClient()
        self.assertIsInstance(paramocko_client, paramikoSSHClient)

    def test_exec_command_stores_its_calls_in_a_dict(self):
        paramocko_client = SSHClient()
        paramocko_client._transport = MagicMock()
        paramocko_client.exec_command("ls")
        self.assertEquals(paramocko_client.exec_command_calls, [("ls", -1, None, False, None)])

    def test_exec_command_stills_returns_a_tuple_of_three(self):
        paramocko_client = SSHClient()
        paramocko_client._transport = MagicMock()
        ret_val = paramocko_client.exec_command("ls")
        self.assertIsInstance(ret_val, tuple)
        self.assertEquals(3, len(ret_val))
