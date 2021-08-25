## Purpose
This script is meant to be used in conjunction with [static_status](https://github.com/Cyclenerd/static_status) page. It extends the static status page by sending E-mail alerts if one of your services is offline.

Since static status has created its own alerting script you get to choose between this script or the original alert.sh that comes with static_status. The difference is: this script uses SMTP for mail notifications while alert.sh uses mutt and allows for additional push or sms notifications.

## Install
Download script and put it into the same directory as your *static_status* webpage or clone this repository onto your server:

`git clone https://github.com/web-pat/static_status_notifications.git`

Edit the script and enter your own E-mail credentials, from-address, to-address, smtp server (line 24).

In order to check for outages the script parses *status.json* which is provided and updated by *static_status* next to the html. Make sure the json-file is present at the location you entered in the script.
If you are running the script from a directory different from your status.json, it's necessary to enter the full path to the file as a parameter in line 32.

## Create Cronjob
In order to check for outages periodically, create a Cronjob

`sudo crontab -e`

and add the following line:

`@hourly /usr/bin/python /path/to/static_status_notification.py`

to run it once every hour or every 30 minutes:

`*/30 * * * * /usr/bin/python /path/to/static_status_notification.py`

It is, of course, sensible to time your cronjob so that it triggers after *static_status* updated.


