import paramiko
import time
host = 'pbx-02.gazelkin.local'
user = 'zazora'
secret = 'qwaszx321'
port = 22
client = paramiko.SSHClient()
time.sleep(1)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('df --output=pcent /')
data = str(stdout.read())
g = str(data[-7:-4]).strip()
print(int(g))
time.sleep(1)
if int(g) >= 90:
    channel = client.get_transport().open_session()
    channel.get_pty()
    channel.settimeout(5)
    channel.exec_command('sudo find /tmp/ -type f -name "*.wav" -delete')
    channel.send(secret+'\n')
    time.sleep(10)
time.sleep(1)
client.close()