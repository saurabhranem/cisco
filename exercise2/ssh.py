from paramiko import SSHClient
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('user@server_id')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
print(ssh_stdout)