def how_many_days(month, year):
    """Function returns number of days for given month, year.
    Leap year definition from wikipedia"""
    if month == 2:
        if year % 4 == 0:
            if year % 100 != 0:
                return 29
            else:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
        else:
            return 28
    if month in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30

#print(how_many_days(2, 752))


