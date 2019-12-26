# Service WatchDog Py - for linux services

Firstly, my website that I host in VPS very often going down. Sometime becouse `mysql` service is not active. Still not yet found the problem, why.

Then I just make this code for running the service that needed for webserver if some of them is going down. In this case I only monitor apache2 and mysql service. (you can add as many as you want)

# Perequisite

## Install Python 3

This code use `python 3` so first you must install it. 

go to https://www.python.org/downloads/

## Set up Cron job 

here the crontab example that run code for every 10 seconds.

`*/10 * * * * cd /home/user/service-watchdog-py/ && /usr/bin/python3.5  /home/user/service-watchdog-py/app.py`

you can change according to your file directory

`*/10 * * * * cd {{ base code directory }} && {{ your python 3 dir}}  {{ file code directory uri }}`