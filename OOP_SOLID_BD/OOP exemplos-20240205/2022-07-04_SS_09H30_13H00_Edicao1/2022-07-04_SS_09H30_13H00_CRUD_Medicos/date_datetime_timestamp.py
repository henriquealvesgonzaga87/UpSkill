# Here, %Y, %m, %d, %H etc. are format codes.
#
# %Y - year [0001,..., 2018, 2019,..., 9999]
# %m - month [01, 02, ..., 11, 12]
# %d - day [01, 02, ..., 30, 31]
# %H - hour [00, 01, ..., 22, 23
# %M - minutes [00, 01, ..., 58, 59]
# %S - second [00, 01, ..., 58, 61]

# >>> from datetime import timedelta
# >>> delta = timedelta(
# ...     days=50,
# ...     seconds=27,
# ...     microseconds=10,
# ...     milliseconds=29000,
# ...     minutes=5,
# ...     hours=8,
# ...     weeks=2
# ... )
# >>> # Only days, seconds, and microseconds remain
# >>> delta
# datetime.timedelta(days=64, seconds=29156, microseconds=10)


from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)


from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

from datetime import datetime
print(datetime.min, datetime.max)
# 0001-01-01 00:00:00 9999-12-31 23:59:59.999999

from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))



from datetime import datetime

# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

#----------
import time
seconds = time.time()
print("Seconds since epoch =", seconds)


import time

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)


import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")


import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)
