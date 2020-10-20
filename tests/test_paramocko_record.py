import unittest

from paramocko import SSHClient
from paramiko import SSHClient as paramikoSSHClient


class TestSSHClient(unittest.TestCase):
    def testSSHClient_is_the_same_type_than_paramiko_ssh_client(self):
        paramocko_client = SSHClient()
        self.assertIsInstance(paramocko_client, paramikoSSHClient)
