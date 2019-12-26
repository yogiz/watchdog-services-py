# Service WatchDog Py - for linux services

Firstly, my website that I host in VPS very often going down. Sometime becouse `mysql` service is not active. Still dont know why.

Then I think, I just need to create code for checking service that needed for webserver if some of them is going down. Then the code will restart the service for me.

In this case I only monitor apache2 and mysql service. (you can add as many as you want)

# Perequisite

## Install Python 3

This code use `python 3` so first you must install it. 

go to https://www.python.org/downloads/

## Set up Cron job 

here the crontab example that run code for every 10 minutes.

`*/10 * * * * cd /home/user/service-watchdog-py/ && /usr/bin/python3.5  /home/user/service-watchdog-py/app.py`

you can change according to your file directory

`*/10 * * * * cd {{ base code directory }} && {{ your python 3 dir}}  {{ file code directory uri }}`

### Cron to delete file one time every month

`0 0 1 * * rm /home/user/WatchDog-Services-Py/log.txt`

Change based on your log uri.

`0 0 1 * * rm {{ log file uri }} `

# Future Imporvement

I want to add features to check if the website is okay thru http request. Then if after restart all service for webserver, the website still down, it will email us and reboot the system.
