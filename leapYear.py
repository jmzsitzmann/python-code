def isLeapYear(xxxx):
    
    if xxxx % 4 == 0:
        if xxxx % 100 == 0:
            if xxxx % 400 == 0:
                return True    
            else:
                 return False
        else:
            return True
    else:
        return False
year = input("what year would you like to check to see if it's a leap year?")
if isLeapYear(year) == True:
    print("Your year is a leap year")
else:
    print("your year is not a leap year") 
        
        