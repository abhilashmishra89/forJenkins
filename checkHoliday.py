import requests
import json
import datetime


def holidayJaList():
    response = requests.get("https://www.googleapis.com/calendar/v3/calendars/japanese__ja%40holiday.calendar.google.com/events?key=AIzaSyBH3GdFIYMMejSq2SSHIh1oQDnLahQ2MDo")
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

#aaj = datetime.datetime.now()
#print(isHoliday('2019-03-21'))

# IMPORTANT:  remove the APIKey before making public !!! 

