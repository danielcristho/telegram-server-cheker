import psutil
import subprocess

#### Disk Usage ####
diskTotal = int(psutil.disk_usage('/').total/(1024*1024*1024))
diskUsed = int(psutil.disk_usage('/').used/(1024*1024*1024))
diskAvailable = int(psutil.disk_usage('/').free/(1024*1024*1024))
diskPercent = psutil.disk_usage('/').percent

#### Memory Usage ####
memTotal = psutil.virtual_memory().total/(1024*1024*1024)
memUsage = psutil.virtual_memory().used/(1024*1024*1024)
memAvailable = psutil.virtual_memory().free/(1024*1024*1024)
memUsagePercent = psutil.virtual_memory().percent

#### CPU Usage ####
cpuUsage = psutil.cpu_percent(interval=1)

####  Uptime Server ####
upTime = subprocess.check_output(['uptime','-p']).decode('UTF-8')

#### Server Description ####
uname = subprocess.check_output(['uname','-rsoi']).decode('UTF-8')
host = subprocess.check_output(['hostname']).decode('UTF-8')
ipAddr = subprocess.check_output(['hostname','-I']).decode('UTF-8')
