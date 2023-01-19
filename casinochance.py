# This program runs a casino-like simulation, except the user gets to choose the dice and the numbers they want.
# It outputs the percent odds of rolling the desired numbers.

def casino():

    numbers = ""

    # error handling
    while len(numbers.split()) != 2:

        numbers = input("Give two numbers, seperated by a space: ")
    
    # split value
    numb = numbers.split()

    die = "foo"
    
    # error handling
    while len(die.split()) != 6:

        die = input("Give six numbers, each corresponding to the sides of a die: ")

    # split value
    ded = die.split()

    a = numb[0]

    b = numb[1]

    # check
    if a not in ded or b not in ded:

        print("0 percent chance")

        return 0
    
    # calculate odds
    chancea = (die.count(a))/6

    chanceb = (die.count(b))/6

    total = chancea * chanceb

    # done
    print("You have a " +str(round(total * 100, 4)) + " percent chance of winning.")

casino()