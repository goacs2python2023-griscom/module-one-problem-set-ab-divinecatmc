import random

def die():

    diceone = random.randint(1,6)

    dicetwo = random.randint(1,6)

    sum = diceone+dicetwo
    if sum == 6 or sum == 7 or sum == 8:

        print(str(sum))

        return ("win")
    
    else:

        print(str(sum))

        return("lose")

print(die())