def casino():
    numbers = ""

    while len(numbers.split()) != 2:

        numbers = input("Give two numbers, seperated by a space: ")
    
    numb = numbers.split()

    die = "foo"
    
    while len(die.split()) != 6:

        die = input("Give six numbers, each corresponding to the sides of a die: ")

    ded = die.split()

    a = numb[0]

    b = numb[1]

    if a not in ded or b not in ded:

        print("0 percent chance")

        return 0
    
    chancea = (die.count(a))/6

    chanceb = (die.count(b))/6

    total = chancea * chanceb

    print("You have a " +str(round(total * 100, 4)) + " percent chance of winning.")

casino()