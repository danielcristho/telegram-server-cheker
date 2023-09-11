from dotenv import load_dotenv
import psutil
import subprocess
import telebot
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

class ServerBot:
    def __init__(self, api_key):
        self.bot = telebot.TeleBot(api_key)

    def start(self):
        @self.bot.message_handler(commands=['start','help'])
        def help(message):
            msg = '''
            Server Monitoring Bot
            ---------
            1. Help → /help
            2. Disk Usage → /disk
            3. CPU and RAM Usage → /sysinfo
            4. Uptime Server → /uptime
            5. Server Description → /server
            ---------
            '''
            self.bot.send_message(message.chat.id, msg)

        # make command function to chat if command receive
        @self.bot.message_handler(commands=['check'])
        def check(message):
            self.bot.send_message(message.chat.id, "The server is alive")

        # disk usage (/disk)
        @self.bot.message_handler(commands=['disk'])
        def disk(message):
            diskTotal = int(psutil.disk_usage('/').total/(1024*1024*1024))
            diskUsed = int(psutil.disk_usage('/').used/(1024*1024*1024))
            diskAvail = int(psutil.disk_usage('/').free/(1024*1024*1024))
            diskPercent = psutil.disk_usage('/').percent

            msg = '''
        Disk Info
        ---------
        Total = {} GB
        Used = {} GB
        Avail = {} GB
        Usage = {} %\n'''.format(diskTotal,diskUsed,diskAvail,diskPercent)
            self.bot.send_message(message.chat.id,msg)

        # cpu & ram (/sysinfo)
        @self.bot.message_handler(commands=['sysinfo'])
        def sysinfo(message):
            cpuUsage = psutil.cpu_percent(interval=1)
            ramTotal = int(psutil.virtual_memory().total/(1024*1024)) #GB
            ramUsage = int(psutil.virtual_memory().used/(1024*1024)) #GB
            ramFree = int(psutil.virtual_memory().free/(1024*1024)) #GB
            ramUsagePercent = psutil.virtual_memory().percent
            msg = '''
        CPU & RAM Info
        ---------
        CPU Usage = {} %
        RAM
        Total = {} MB
        Usage = {} MB
        Free  = {} MB
        Used = {} %\n'''.format(cpuUsage,ramTotal,ramUsage,ramFree,ramUsagePercent)
            self.bot.send_message(message.chat.id,msg)

        #uptime (/uptime)
        @self.bot.message_handler(commands=['uptime'])
        def uptime(message):
            upTime = subprocess.check_output(['uptime','-p']).decode('UTF-8')
            msg = upTime
            self.bot.send_message(message.chat.id,msg)

        #server desc (/server)
        @self.bot.message_handler(commands=['server'])
        def server(message):
            uname = subprocess.check_output(['uname','-rsoi']).decode('UTF-8')
            host = subprocess.check_output(['hostname']).decode('UTF-8')
            ipAddr = subprocess.check_output(['hostname','-I']).decode('UTF-8')
            msg ='''
        Server Desc
        ---------
        OS = {}
        Hostname = {}
        IP Addr = {}'''.format(uname,host,ipAddr)
            self.bot.send_message(message.chat.id,msg)

        #listen to telegram commands
        self.bot.polling()
