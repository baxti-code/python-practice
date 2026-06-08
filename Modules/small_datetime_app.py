import datetime 
import random

# def day_counter():
#     date1 = input("Enter the first date (format : YYY-MM-DD): ")
#     date2 = input("Enter the second date (format : YYY-MM-DD): ")
#     d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
#     d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
#     result = d2 -d1
#     return result.days

# if __name__ == "__main__":
#     print(day_counter())


import datetime
import random

# 1-Modul: Faqat tasodifiy sana generatsiya qiladi
def generate_random_date():
    today = datetime.date.today()
    random_days = random.randint(1, 365)
    future_date = today + datetime.timedelta(days=random_days)
    return future_date  # Faqat sanani qaytaradi, necha kun qo'shganini yashiradi

# 2-Modul: Berilgan sanagacha necha kun qolganini hisoblaydi
def calculate_days_until(target_date):
    today = datetime.date.today()
    # Bu funksiya orqada nima bo'lganidan bexabar, shunchaki sof hisob-kitob qiladi
    difference = (target_date - today).days
    return difference

# --- Dasturni ishlatib ko'ramiz ---

# Bazaga tasodifiy sana yozildi deb tasavvur qilamiz
random_date = generate_random_date() 
print(f"Bazada saqlangan sana: {random_date.strftime('%B %d, %Y')}")

# Butunlay boshqa joyda o'sha sanagacha muddatni hisoblaymiz
number_of_days = calculate_days_until(random_date)
print(f"Ushbu sanagacha {number_of_days} kun bor.")