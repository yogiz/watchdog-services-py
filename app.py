import subprocess
from datetime import datetime
import os


now = datetime.now()
curTime = now.strftime("%d/%m/%y - %H:%M")

services = ["mysql", "apache2"] # change, add service you want watch
needReboot = False

with open('log.txt', 'a') as f:
        f.writelines(curTime + "  :\n")

for service in services :

        status = ''
        p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')

        if(output == 'inactive\n'):
                try :
                        os.system('sudo /etc/init.d/'+ service +' start')
                        status = ' ---  succes running \n'
                except :
                        status = ' ---  fail running fixer \n'
                        needReboot = True

        with open('log.txt', 'a') as f:
                f.writelines( '  ' + service +' - ' + output + status)

if(needReboot):
        os.system("sudo reboot")