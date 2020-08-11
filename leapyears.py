def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year %  100 != 0 )


year = int(input())
if year >=1900 and year <=10**5:
    print(is_leap(year))