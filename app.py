from services import run_checker
from mailer import mail_tester

### SET UP SERVICES ###
services = ["mysql", "apache2"] # change, add service you want watch

### SET UP EMAIL - here is the example setting ###
isEmail = False  # set True    if you want turn on email notif feature
# ------------ [ssl (True/False), port, smtp_server, login, password, sender, receiver]
mail_setting = [True, 465, "smtp.example.com","from@example.com", "1a2b3c4d5e6f7g", "from@example.com", "receiver@example.com"] 


### RUN SERVICES 

# test Email
# mail_tester(mail_setting) 

# Run
run_checker(services, isEmail, mail_setting)