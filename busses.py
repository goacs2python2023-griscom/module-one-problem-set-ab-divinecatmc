
# This program will calculate the number of busses to accommodate an inputted amount of passengers. Each bus carries 52.

def bus():

    # input people
    people = input("Enter passenger number: ")

    # number crunching
    div = int(people) / 52

    remainder = int(people)//52

    # if there's a remainder, add an extra bus
    if div > remainder:

        remainder += 1
    
    # and there we go!
    print("You need "+ str(remainder) + " busses to fit everyone")

    return(remainder)

bus()


