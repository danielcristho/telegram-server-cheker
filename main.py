from command import ServerBot
from collector import ServerConnector
import yaml

if __name__ == "__main__":
    server_bot = ServerBot(API_KEY)

    with open('inventory.yaml', 'r') as file:
        servers = yaml.load(file, Loader=yaml.FullLoader)['servers']


    server_connector = ServerConnector(servers)
    server_connector.connect_all_servers()

    server_bot.start()