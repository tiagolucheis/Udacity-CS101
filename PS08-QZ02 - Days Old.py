# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysOfmonth(month, year):
    if month < 8:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            if month % 2 == 0:
                return 30
            else:
                return 31
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    if year1 == year2:
        if month1 == month2:
            if day1 == day2:
                return 0
            elif day1 > day2:
                return daysBetweenDates(year1, month1, 1, year2, month2, day2) - (day1 - 1)
            else:
                return 1 + daysBetweenDates(year1, month1, day1 + 1, year2, month2, day2)
        else:
            return daysOfmonth(month1, year1) + daysBetweenDates(year1, month1 + 1, day1, year2, month2, day2)
    elif year2 - year1 == 1:
        if month1 % 12:
            return daysOfmonth(month1, year1) + daysBetweenDates(year1, month1 + 1, day1, year2, month2, day2)
        else:
            return daysOfmonth(month1, year1) + daysBetweenDates(year1 + 1, 1, day1, year2, month2, day2)
    else:
        if isLeapYear(year1):
            return 366 + daysBetweenDates(year1 + 1, month1, day1, year2, month2, day2)
        else:
            return 365 + daysBetweenDates(year1 + 1, month1, day1, year2, month2, day2)

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()