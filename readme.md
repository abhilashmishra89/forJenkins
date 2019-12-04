
* Works for the customised asterisk extension check. The script sipstatus.py need to be configured in crontab to run every 10 minute.

* */10 * * * 1,2,3,4,5 python /home/ncc/sipstatus.py *

* Add a file conf_data.py in the working directory in the below format, as it has critical data, it should always be included in the gitignore

```
smtp_id = 'smtp.gmail.com'
smtp_password = 'smtp-password'
fromEmail = "fromemail@example.com"
toEmail = ['toemail-1@example.com.jp,toemail-2@example.com']
key = 'read here how to get it : https://developers.google.com/maps/documentation/javascript/get-api-key'
html = """\
<!DOCTYPE html>
<html>
<body>

<h1>This is the header of sample Email Alert</h1>
<h3>
This is the static message configured to be sent as alert in h3 tag.

</h3>
<a href="http://192.168.188.130:8786/monitoring_tool/index.php">NCC Extension status</a>

</body>
</html>
"""

```
Functionality:
 
    1. script checkHoliday checks the list of holidays in Japan.
  
    2. sipstatus script checks the status of asterisk extensions, If unregistered and it is not holiday in japan, it sends email alert to the preconfigured email id's (toEmail)
  
  
