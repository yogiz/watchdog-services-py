import subprocess
from time import ctime
import os
from mailer import send_mail

def check_service(service) :
    p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    output = output.decode('utf-8')
    return output

def run_checker(services, isEmail, mail_setting) :
    needReboot = False

    for service in services :

        status = ''
        output = check_service(service)

        if(output == 'inactive\n'):
            try :
                os.system('sudo /etc/init.d/'+ service +' start')
                status = ' ---  succes restart the services \n'
            except :
                status = ' ---  fail restart services \n'
                needReboot = True

            if (check_service(service) == 'inactive\n') :
                needReboot = True

            curTime = ctime()
            message = curTime + ' : ' + service +' - ' + output + status
            with open('log.txt', 'a') as f:
                f.writelines(message)  
            if isEmail :
                subject = "Service Watcher update - " + curTime
                send_mail(message, subject, mail_setting)
                    
    if(needReboot):
        os.system("sudo reboot")