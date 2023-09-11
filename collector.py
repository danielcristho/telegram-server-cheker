import paramiko
import yaml

class ServerConnector:

    def __init__(self, servers):
        self.servers = servers

    def connect_to_server(self, ip, username, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password)
        return client

    def connect_all_servers(self):
        for server in self.servers:
            ip = server['ip']
            username = server['username']
            password = server['password']

            ssh_client = self.connect_to_server(ip, username, password)
            ssh_client.close()