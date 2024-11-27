import datetime
import pytz #converting time between different timezones
timezone = pytz.timezone('UTC')
tz = datetime.datetime.now(timezone)
print(tz)

x = datetime.datetime.now()
print(x.year)
print(x.strftime('%B'))#month
future= x + datetime.timedelta(days=10)#add or subtract to current datetime using timedelta
print(future)

y = datetime.datetime(2008, 5, 6)
print(y.strftime('%A'))#day of the week

z = '2024-12-25'
obj= datetime.datetime.strptime(z,'%Y-%m-%d')#coverting string to date
print(obj)

