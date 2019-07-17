# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
#use the code snippets from main file sipstatus.py for testing purpose.
#test any changes here before changing sipstatus.py file.
#
me = "ncc@extensioncheck.com"
#you = "zb_ameyotech@ipsism.co.jp"
you = "abhilash@ipsism.co.jp,vijay@ipsism.co.jp"
#you = "abhilash@ipsism.co.jp"
#
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test Code, testing multiple recepients, Ignore"
msg['From'] = me
msg['To'] = you
#
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
os.system("echo 'bhangbhosada' > /tmp/trigger")
if os.stat("/tmp/trigger").st_size != 0:
    s.sendmail(me, you, msg.as_string())
    s.quit()
