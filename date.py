import datetime
import calendar


def findday(date):
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return calendar.day_name[day]


date = input("Enter the date in format of 'date month year'")
print(findday(date))
