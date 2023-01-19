def dates():
        
    print("For this project, I will need two dates. Input the dates accordingly.")

    day_a = "bar"
    
    month_a = "bosh"
    
    year_a = "foo"
    
    while day_a.isdigit() == False:

        day_a = input("Day 1: ")
    
    int(day_a)

    while month_a.isdigit() == False:

        month_a = input("Month 1: ")

    int(month_a)

    while year_a.isdigit() == False:

        year_a = input("Year 1: ")

    int(year_a)

    day_b = "bar"
    
    month_b = "bosh"
    
    year_b = "foo"

    while day_b.isdigit() == False:

        day_b = input("Day 2: ")
    
    int(day_b)

    while month_b.isdigit() == False:

        month_b = input("Month 2: ")

    int(month_b)

    while year_b.isdigit() == False:

        year_b = input("Year 2: ")

    int(year_b)

    # Now we compare the two, oh boy

    if year_a == year_b:

        if month_a == month_b:

            if day_a == day_b:

                return "equal"
            
            if day_a > day_b:

                return "first"
            
            else:

                return "second"
            
        elif month_a > month_b:

            return "first"
    
        else:

            return "second"
          
    elif year_a > year_b:

        return "first"
    
    else:

        return "second"


date = dates()

if date == "equal":

    print("Same")

elif date == "first":

    print("Before")

else:

    print("After")