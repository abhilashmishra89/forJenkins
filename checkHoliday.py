import requests
import json
import datetime
from conf_data import key


def holidayJaList():
    response = requests.get(
        "https://www.googleapis.com/calendar/v3/calendars/japanese__ja@holiday.calendar.google.com/events?key={0}".format(key))
    data = response._content
    simple_data = json.loads(data)
    item = simple_data['items']
    dates = []
    # print(item)
    for element in item:
        dates.append(element['start']['date'])
    return dates


def isHoliday(aaj):
    if aaj in holidayJaList():
        return True
    else:
        return False
