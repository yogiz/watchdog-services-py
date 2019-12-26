import subprocess
from datetime import datetime
import os

def check_service(service) :
        p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')
        return output

services = ["mysql", "apache2"] # change, add service you want watch
needReboot = False

for service in services :

        status = ''
        output = check_service(service)

        if(output == 'inactive\n'):
                try :
                        os.system('sudo /etc/init.d/'+ service +' start')
                        status = ' ---  succes running \n'
                except :
                        status = ' ---  fail running fixer \n'
                        needReboot = True

                if (check_service(service) == 'inactive\n') :
                        needReboot = True

                now = datetime.now()
                curTime = now.strftime("%d/%m/%y - %H:%M")
                with open('log.txt', 'a') as f:
                        f.writelines( curTime + ' : ' + service +' - ' + output + status)        

if(needReboot):
        os.system("sudo reboot")