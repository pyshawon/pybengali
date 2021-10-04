# -*- coding: utf-8 -*-
import os
import sys
BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"."))
sys.path.insert(0, BASEDIR)
import pybengali

print(pybengali.past_date('2'))
print(pybengali.future_date('2'))
print(pybengali.bengali_numbers())
print(pybengali.bengali_months())
print(pybengali.bengali_weekdays())
print(pybengali.bengali_seasons())
print(pybengali.get_year(day="04", month="10", year="2021"))
print(pybengali.get_weekday(day="04", month="10", year="2021"))
print(pybengali.convert_e2b_digit('10'))
print(pybengali.yesterday())
print(pybengali.today())
print(pybengali.today(day="04", month="10", year="2022"))
print(pybengali.tomorrow())
print(pybengali.timesince(day="04",month="10", year="2019"))
print(pybengali.eng_month_to_bengali("1"))
