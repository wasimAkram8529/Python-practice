from datetime import datetime

now = datetime.now()

print(now.date())
print(now.time())
print(now.day)
print(now.minute)
dateTime_string = now.strftime("%d:%m:%Y %H:%M %p")

print(dateTime_string)

dateTime_object = datetime.strptime(dateTime_string, "%d:%m:%Y %H:%M %p")
print(dateTime_object)
