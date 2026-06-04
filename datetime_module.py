# from datetime import datetime

# now = datetime.now()

# # print(now.year)    # yil
# # print(now.month)   # oy
# # print(now.day)     # kun
# # print(now.hour)    # soat
# # print(now.minute)  # daqiqa
# # print(now.second)  # soniya
# print(now.strftime("%Y-%m-%d"))
# print(now.strftime("%H %p"))
# print(now.strftime("%B %A"))

# from datetime import datetime, timedelta

# now = datetime.now()

# # 7 kun keyin
# future = now + timedelta(days=7)
# print(future.strftime("%Y-%m-%d"))

# # 7 kun oldin
# past = now - timedelta(days=7)
# print(past.strftime("%Y-%m-%d"))

# from datetime import datetime

# birthday = datetime(2007, 5, 5)
# now = datetime.now()

# difference = now - birthday
# print(f"Siz {difference.days} kun yashadingiz!")

# from datetime import datetime

# date_string = "2026-01-15"
# date = datetime.strptime(date_string, "%Y-%m-%d")

# print(date)
# print(type(date))
# print(date.year)

from datetime import datetime

now = datetime.now()
day_of_year = now.strftime("%j")
day_of_week = now.strftime("%A")

print(f"Bugun yilning {day_of_year}-kuni")
print(f"Bugun {day_of_week}")