# -*- coding: utf-8 -*-
import datetime

last_day_of_bengali_months =  [13, 12, 14, 13, 14, 14, 15, 15, 15, 15, 14, 14]
bn_months_days = [30, 30, 30, 30, 31, 31, 31, 31, 31, 30, 30, 30]
bn_number = ['০', '১','২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
en_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
bn_months = ["পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র", "বৈশাখ", "জ্যৈষ্ঠ", "আষাঢ়", "শ্রাবণ", "ভাদ্র", "আশ্বিন", "কার্তিক", "অগ্রহায়ণ"]
bn_weekdays = ["সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার", "শনিবার", "রবিবার"]
bn_seasons = ["শীত", "বসন্ত", "গ্রীষ্ম", "বর্ষা", "শরৎ", "হেমন্ত"]


def bengali_numbers():
    return bn_number

def bengali_months():
    return bn_months

def bengali_weekdays():
    return bn_weekdays

def bengali_seasons():
    return bn_seasons

def convert_e2b_digit(digits):
    try:
        bengali_digit = ""
        for digit in str(digits):
            if digit in en_number:
                bengali_digit+=bn_number[en_number.index(digit)]
            else:
                bengali_digit+=digit
        return bengali_digit
    except Exception as e:
        print("Please Make sure you have passed parameter in right format convert_e2b_digit('10')")


def check_leap_year(year):
    return True if int(year) % 400 == 0 else True if int(year) % 4 == 0 and int(year) % 100 != 0 else False

def get_year(day, month, year):
    try:
        return convert_e2b_digit(int(year) - 593 if int(month) > 3 else int(year) - 593 if int(month) == 3 and int(day) > 13 else int(year) - 594)
    except Exception as e:
        print('Please Make sure you have passed parameter in right format get_year(date="04", month="10", year="2021")')

def get_weekday(day, month, year):
    try:
        return bn_weekdays[datetime.datetime(int(year), int(month), int(day)).weekday()]
    except Exception as e:
        print('Please Make sure you have passed parameter in right format get_weekday(day="04", month="10", year="2021")')

def today(day=None, month=None, year=None):
    if day == None and month == None and year == None:
        current_date_object = datetime.date.today()
        year = current_date_object.year
        month = current_date_object.month
        day = current_date_object.day
    else:
        day = int(day)
        month = int(month)
        year = int(year)

    bengali_weekday = get_weekday(day, month, year)
    month = month - 1
    bengali_year = get_year(day, month, year)

    if day <= last_day_of_bengali_months[month]:
        total_days_in_current_bengali_month = bn_months_days[month]
        if month == 2 and is_leap_year(year) == 1:
            total_days_in_current_bengali_month += 1
        bengali_date = total_days_in_current_bengali_month + day - last_day_of_bengali_months[month]
        bengali_month_index = month
        bengali_month = bn_months[bengali_month_index]
    else:
        bengali_date = day - last_day_of_bengali_months[month]
        bengali_month_index = (month+1)%12
        bengali_month = bn_months[bengali_month_index]

    bengali_season = bn_seasons[bengali_month_index // 2]

    bengali_date_month_year_season = {
        "date": convert_e2b_digit(bengali_date),
        "month": convert_e2b_digit(bengali_month),
        "year": bengali_year,
        "season": convert_e2b_digit(bengali_season),
        "weekday": convert_e2b_digit(bengali_weekday)
    }

    return bengali_date_month_year_season


def past_date(day):
    date_object = datetime.date.today() - datetime.timedelta(days = int(day))
    return today(
        day=date_object.day, 
        month=date_object.month, 
        year=date_object.year
    )

def future_date(day):
    date_object = datetime.date.today() + datetime.timedelta(days = int(day))
    return today(
        day=date_object.day, 
        month=date_object.month, 
        year=date_object.year
    )

def yesterday():
    return past_date(1)

def tomorrow():
    return future_date(1)


def timesince(day, month, year):
    try:
        dt = datetime.datetime(int(year),int(month),int(day))
        now = datetime.datetime.now()
        diff = now - dt
        periods = (
            (diff.days / 365, "বছর", "বছর"),
            (diff.days / 30, "মাস", "মাস"),
            (diff.days / 7, "সপ্তহ", "সপ্তহ"),
            (diff.days, "দিন", "দিন"),
            (diff.seconds / 3600, "ঘন্টা", "ঘন্টা"),
            (diff.seconds / 60, "মিনিট", "মিনিট"),
            (diff.seconds, "সেকেন্ড", "সেকেন্ড"),
        )
        for p, s1, s2 in periods:
            if p >= 1:
                return "{} {} আগে".format(convert_e2b_digit(int(p)), s1 if p == 1 else s2)
        return default
    except Exception as e:
        print('Please Make sure you have passed parameter in right format timesince(date="04", day="10", year="2021")')


def eng_month_to_bengali(month_number):
    months = [ 'জানুয়ারী', 'ফেব্রুয়ারী', 'মার্চ', 'এপ্রিল', 'মে', 'জুন', 'জুলাই', 'আগস্ট', 'সেপ্টেম্বর', 'অক্টোবর', 'নভেম্বর', 'ডিসেম্বর' ]
    return months[int(month_number) -1]

