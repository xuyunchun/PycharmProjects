# -*- coding:utf-8 -*-
import paramikodef

sftp_exec_command(command):
try:        ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(host, 22, user, password)
std_in, std_out, std_err = ssh_client.exec_command(command)
for line in std_out:            print line.strip("/n")
ssh_client.close()    except Exception, e:        print eif
__name__ == '__main__':    sftp_exec_command("ls -l")
