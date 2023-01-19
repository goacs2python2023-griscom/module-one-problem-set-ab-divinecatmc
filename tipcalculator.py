# This one calculates the tips, by asking for the bill and the percent tips, then doing some math to add the bill and the 
# tip.

def tips():

    bill = int(input("What is the bill? "))

    percent = int(input("What percent tip do you want to give? (just a number): "))

    tip = (percent / 100) * bill

    total = tip + bill

    print("Your bill totals " + total + " units of currency.")

tips()
