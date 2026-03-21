from datetime import datetime
now=datetime.now()
print(now)
print(now.hour)
print(now.strftime('%d/%m/%Y, %H:%M:%S'))
date_string = "5 December, 2019"
date_object=(datetime.strptime(date_string,'%d %B, %Y'))
print(date_object)
