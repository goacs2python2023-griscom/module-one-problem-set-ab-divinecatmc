def years():

    year = int(input("Insert year: "))

    if year % 100 == 0:
        
        if year % 400 == 0:

            return True
        
        else:

            return False
    
    elif year % 4 == 0:

        return True

    return False

print(years())