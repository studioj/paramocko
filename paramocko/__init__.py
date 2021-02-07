from paramiko import SSHClient as ParamikoSSHClient

__version__ = "0.0.1"


class SSHClient(ParamikoSSHClient):
    _recording = False

    def __init__(self):
        super().__init__()
        self.exec_command_calls = []

    def exec_command(self, command, bufsize=-1, timeout=None, get_pty=False, environment=None):
        if self._recording:
            self.exec_command_calls.append((command, bufsize, timeout, get_pty, environment))
        return super(SSHClient, self).exec_command(
            command=command,
            bufsize=bufsize,
            timeout=timeout,
            get_pty=get_pty,
            environment=environment,
        )

    def start_recording(self):
        self._recording = True

    def stop_recording(self):
        self._recording = False
