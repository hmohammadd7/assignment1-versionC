#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py
The python code in this file is original work written by
"Hassnain Mohammad". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Hassnain Mohammad
Semester: Fall 2024
Description: Assignment 1 - Version C
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"

#Not a leap year
    lyear = year % 4

    if lyear == 0:

        leap_flag = True

    else:

        leap_flag = False

#Not a leap year
    lyear = year % 100

    if lyear == 0:

        leap_flag = False

#Is a leap year
    lyear = year % 400

    if lyear == 0:

        leap_flag = True

#If leap year will return True
    return leap_flag



def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

#To check leap year
    leap_flag = leap_year(year)

    if month == 2 and leap_flag:

        return 29

    else:

        return mon_dict[month]


def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''

#Next day
    day, mon, year = (int(x) for x in date.split('/'))

    day += 1

#To check leap year
    leap_flag = leap_year(year)

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if mon == 2 and leap_flag:

        mon_max = 29

    else:

        mon_max = mon_dict[mon]

    if day > mon_max:

        mon += 1

        if mon > 12:

            year += 1

            mon = 1

        day = 1  #If tmp_day > this month's max, reset to 1

    return f"{day:02}/{mon:02}/{year}"


def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"

#Next day
    day, mon, year = (int(x) for x in date.split('/'))

    day -= 1

#Takes you to previous month
    if day == 0:

        mon -= 1

        if mon == 0:

            year -= 1 #Takes you to previous year

            mon = 12 #The month is to be December

#To check for the leap year
        if mon == 2:

            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day = 29

            else:
                day = 28

        else:
            mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

            day = mon_dict[mon]

    return f"{day:02}/{mon:02}/{year}"


def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    print("The user input is invalid")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"

#To split the dates into parts
    parts = date.split('/')

#To check day, month and year
    if len(parts) != 3:

        return False

    day_str = parts[0]

    mon_str = parts[1]

    year_str = parts[2]

#To check for numbers
    day_is_digit = day_str.isdigit()

    month_is_digit = mon_str.isdigit()

    year_is_digit = year_str.isdigit()

    if day_is_digit == False:

        return False

    if month_is_digit == False:

        return False

    if year_is_digit == False:

        return False


    day = int(day_str)

    mon = int(mon_str)

    year = int(year_str)

#To check for month
    if mon < 1:

        return False

    if mon > 12:

        return False

#To see if number of days are in a month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#To check leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

        days_in_month[1] = 29  #To check the leap year for February

#To confirm the days of the month
    if day < 1 or day > days_in_month[mon - 1]:

        return False

    return True  #To check if the date is valid



def check_number(num: str) -> bool:
    """
    check second argument is the right number
    """

#If number starts with negative sign
    if num[0] == '-':

#If other strings are numbers
        return num[1:].isdigit()

#Checking if all strings are numbers
    return num.isdigit()



def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"

    date = start_date

    while num != 0:

#Navigate to the next day
        if num > 0:

            date = after(date)

            num -= 1

#Navigate to the previous day
        else:

            date = before(date)

            num += 1

    return date



if __name__ == "__main__":

#Check length of arguments
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]

    days_count_str = sys.argv[2]

#Check first arg is a valid date
    if valid_date(start_date) == False:
        usage()

#Check that second arg is a valid number (+/-)
    if check_number(days_count_str) == False:
        usage()

#Convert second argument to integer "int()"
    days_count = int(days_count_str)

#Call day_iter function to get end date, save to x
    final_date = day_iter(start_date, days_count)

#Print(f'The end date is {day_of_week(x)}, {x}.')
    weekday_name = day_of_week(final_date)

    print(f"The end date is {weekday_name}, {final_date}.")

    pass
