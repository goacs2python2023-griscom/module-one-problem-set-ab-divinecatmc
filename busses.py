
def bus():

    people = input("Enter passenger number: ")

    div = int(people) / 52

    remainder = int(people)//52

    if div > remainder:

        remainder += 1
    
    
    print("You need "+ str(remainder) + " busses to fit everyone")

    return(remainder)

bus()


