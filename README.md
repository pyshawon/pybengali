# PYBENGALI
pybengali is a python3 package for Bengali DateTime and Bengali numeric number conversation and many more. This package can be used with any python framework like Django, Flask, FastAPI, and others. pybengali is OS Independent, It can be used on any operating system Linux/Unix, Mac OS and Windows.


## Available Features
-   Features available in pybengali:
   - List of Bengali Numbers
   - List of Bengali Months
   - List of Bengali Weekdays
   - List of Bengali Seasons
   - Bengali Year
   - Bengali Weekday
   - Bengali Date 
   - Bengali Today
   - Bengali Tomorrow
   - Bengali Yesterday
   - Bengali Past Date
   - Bengali Future Date
   - Bengali Timesince
   - Convert English Month Name to Bengali
   - Convert English Numeric Number to Bengali Numeric Number


# Installation
```bash
$ pip install pybengali
```

# Usage

Get Bengali Today:
```python
import pybengali
today = pybengali.today()
print(today)
# Output: {'date': '১৯', 'month': 'আশ্বিন', 'year': '১৪২৮', 'season': 'শরৎ', 'weekday': 'সোমবার'}

today = pybengali.today(day="04", month="10", year="2022")
print(today)
# Output: {'date': '১৯', 'month': 'আশ্বিন', 'year': '১৪২৯', 'season': 'শরৎ', 'weekday': 'মঙ্গলবার'}
```


Get Bengali Tomorrow and Yesterday:
```python
import pybengali
tomorrow = pybengali.tomorrow()
print(tomorrow)
# Output: {'date': '২০', 'month': 'আশ্বিন', 'year': '১৪২৮', 'season': 'শরৎ', 'weekday': 'মঙ্গলবার'}

yesterday = pybengali.yesterday(day="04", month="10", year="2022")
print(yesterday)
# Output: {'date': '১৮', 'month': 'আশ্বিন', 'year': '১৪২৮', 'season': 'শরৎ', 'weekday': 'রবিবার'}
```

Get Bengali Timesince:
```python
import pybengali
timesince = pybengali.timesince(day="04",month="10",year="2019")
print(timesince)
# Output: ২ বছর আগে
```

Get Bengali Past or Future Date With Number of Days To Go Back or Froward :
```python
import pybengali
# Past Date
past_date = pybengali.past_date('2')
print(past_date)
# Output: {'date': '১৭', 'month': 'আশ্বিন', 'year': '১৪২৮', 'season': 'শরৎ', 'weekday': 'শনিবার'}

# Future Date
future_date = pybengali.future_date('2')
print(future_date)
# Output: {'date': '২১', 'month': 'আশ্বিন', 'year': '১৪২৮', 'season': 'শরৎ', 'weekday': 'বুধবার'}
```

Get Bengali Year:
```python
import pybengali
year = pybengali.get_year(day="04", month="10", year="2021")
print(year)
# Output:  ১৪২৮
```

Get Bengali Weekday:
```python
import pybengali
weekday = pybengali.get_weekday(day="04", month="10", year="2021")
print(weekday)
# Output:  সোমবার
```

Convert English Numeric Number to Bengali Numeric Number:
```python
import pybengali
bengali_digit = pybengali.convert_e2b_digit("10")
print(bengali_digit)
# Output:  ১০
```

Convert English Month  to Bengali Name:
```python
import pybengali
bengali_name = pybengali.eng_month_to_bengali("1")
print(bengali_name)
# Output:  জানুয়ারী
```

Get List of Bengali Numbers:
```python
import pybengali
numbers = pybengali.bengali_numbers()
print(numbers)
# Output:  ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
```

Get List of Bengali Months:
```python
import pybengali
months = pybengali.bengali_months()
print(months)
# Output:  ['পৌষ', 'মাঘ', 'ফাল্গুন', 'চৈত্র', 'বৈশাখ', 'জ্যৈষ্ঠ', 'আষাঢ়', 'শ্রাবণ', 'ভাদ্র', 'আশ্বিন', 'কার্তিক', 'অগ্রহায়ণ']
# Months sequence Is accroding to English calender.
```


Get List of Bengali Weekdays:
```python
import pybengali
weekdays = pybengali.bengali_weekdays()
print(weekdays)
# Output:  ['সোমবার', 'মঙ্গলবার', 'বুধবার', 'বৃহস্পতিবার', 'শুক্রবার', 'শনিবার', 'রবিবার']
# weekdays sequence Is accroding to English calender.
```


Get List of Bengali Seasons:
```python
import pybengali
seasons = pybengali.bengali_seasons()
print(seasons)
# Output:  ['শীত', 'বসন্ত', 'গ্রীষ্ম', 'বর্ষা', 'শরৎ', 'হেমন্ত']
# seasons sequence Is accroding to English calender.
```

*pybengali is build based on Bengali calendar which was officially adopted in Bangladesh in 1987 and All the rules from [Bengali_calendars](https://en.wikipedia.org/wiki/Bengali_calendars  "Bengali_calendars") to convert Gregorian date to Bangla date. *

# Contribute
If you face any problem feel free to open issue.

# Contact
If you have any suggestion:
Email: pyshawon@gmail.com
Facebook: https://www.facebook.com/pyshawon/



