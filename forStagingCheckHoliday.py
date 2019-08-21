# -*- coding: utf-8 -*-
import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
import requests
import json

def holidayJaList():
    response = requests.get("https://www.googleapis.com/calendar/v3/calendars/indian__en%40holiday.calendar.google.com/events?key=AIzaSyB8pk8pEuZ_MlDyknetsNdgmlQNPatu-x8")
    data = response._content
    simple_data = json.loads(data)
    item= simple_data['items']
    dates=[]
    #print(item)
    for element in item:
        dates.append(element['start']['date'])    
    return dates

def isHoliday(aaj):
    if aaj in holidayJaList():
        return True
    else:
        return False
# aaj = '2019-08-12'
# print(isHoliday(aaj))

me = "asterisk@extensioncheck.com"
you = ['abhilash@ipsism.co.jp','abhilashmishra89@gmail.com']
#you = "abhilash@ipsism.co.jp,lalala@gmail.com" #comma seperated values are ok

msg = MIMEMultipart('alternative')
msg['Subject'] = "Extension Unregistered"
msg['From'] = me
msg['To'] = ", ".join(you)

html="""\	
<!DOCTYPE html>
<html>
<body>

<h1>国立がんセンターの内線番号がUnregisteredになりました。
至急以下へご連絡をお願い致します。</h1>
<h3>
国立がんセンター連絡先：03-3547-5201 内線1616
担当：澤井様、桜井様、小野様
</h3>
<a href="http://192.168.188.130:8786/monitoring_tool/index.php">NCC Extension status</a>

</body>
</html>
"""
part2 = MIMEText(html, 'html')
msg.attach(part2)
s = smtplib.SMTP('localhost')
d= datetime.datetime.now()
flag = date.today()
isholiday = False
if isholiday is False:
    if d.hour in range(10,15): #configure the time for which the script should work. Right now it is 10 AM to 03:00 PM.
        os.system("rm -rf /tmp/trigger")
        os.system("/dacx/ameyo/asterisks/13/sbin/asterisk -C /dacx/var/ameyo/dacxdata/asterisks/13/etc/asterisk/asterisk.conf -rx 'sip show peers' | grep Unspecified >>/tmp/trigger")
        if os.stat("/tmp/trigger").st_size != 0:
            s.sendmail(me, you, msg.as_string())
            s.quit()
