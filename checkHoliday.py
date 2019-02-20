import requests
import json
import datetime


def holidayJaList():
    response = requests.get("https://www.googleapis.com/calendar/v3/calendars/japanese__ja%40holiday.calendar.google.com/events?key=APIkeyfromgoogle")
    data = response._content
    simple_data = json.loads(data)
    item= simple_data['items']
    chugal=[]
    #print(item)
    for element in item:
        chugal.append(element['start']['date'])    
    return chugal

def isHoliday(aaj):
    if aaj in holidayJaList():
        return True
    else:
        return False

#checkCommit