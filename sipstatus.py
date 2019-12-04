# -*- coding: utf-8 -*-
import datetime
import os
import smtplib
from checkHoliday import isHoliday, holidayJaList
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from conf_data import fromEmail, toEmail, smtp_id, smtp_password


msg = MIMEMultipart('alternative')
msg['Subject'] = "NCC Extension Unregistered"
msg['From'] = fromEmail
msg['To'] = ", ".join(toEmail)

html = """\
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
s = smtplib.SMTP('smtp.gmail.com', 587)
d = datetime.datetime.now()
flag = str(date.today())
isholiday = isHoliday(flag)
if isholiday is False:
    if d.hour in range(10, 15):
        os.system("rm -rf /tmp/trigger")
        os.system("/dacx/ameyo/asterisks/1.6/sbin/asterisk -C /dacx/var/ameyo/dacxdata/asterisks/1.6/etc/asterisk/asterisk.conf -rx 'sip show peers' | grep Unspecified >>/tmp/trigger")
        if os.stat("/tmp/trigger").st_size != 0:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('{0}'.format(smtp_id), '{0}'.format(smtp_password))
            s.sendmail(fromEmail, toEmail, msg.as_string())
            s.quit()
