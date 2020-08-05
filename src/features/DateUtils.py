def isLeapYear(year):
    try:
        if year < 0:
            raise ValueError
        result = False
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            result = True
        return result
    except ValueError: print("PLop")

#For debug only
if __name__ == "__main__":
    print("We launch DateUtils.py")