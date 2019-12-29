import smtplib
from socket import gaierror
from time import ctime

def send_mail(message, subject, mail_setting) :
    port = mail_setting[1] 
    smtp_server = mail_setting[2]
    login = mail_setting[3]
    password = mail_setting[4]
    sender = mail_setting[5]
    receiver = mail_setting[6]

    # type your message: use two newlines (\n) to separate the subject from the message body, and use 'f' to  automatically insert variables in the text
    message = """Subject: %s
To: %s
From: %s

%s""" % (subject,receiver,sender,message)

    try:
        #send your message with credentials specified above
        if(mail_setting[0]) :
            with smtplib.SMTP_SSL(smtp_server, port) as server:
                server.login(login, password)
                server.sendmail(sender, receiver, message)
        else :
            with smtplib.SMTP(smtp_server, port) as server:
                server.login(login, password)
                server.sendmail(sender, receiver, message)
        # tell the script to report if your message was sent or which errors need to be fixed 
        write_log('Email sent to ' + receiver)
    except (gaierror, ConnectionRefusedError):
        write_log('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        write_log('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        write_log('SMTP error occurred: ' + str(e))

def write_log(message) :
    with open('mailer_log.txt', 'a') as f:
        now = ctime()
        f.writelines(now + ' : - ' + message + '\n\n')

def mail_tester(mail_setting) :
    send_mail('This is test email from Wathdog-Services-Py', 'Wathdog Services Test', mail_setting)