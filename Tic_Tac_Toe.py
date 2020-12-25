from classes import Board


user = ""
AI = ""


def starting():
    starting = input("Do you want to start (Y/N)? ").upper()
    inputUnderstood = False
    while inputUnderstood == False:
        if starting == "Y":
            user = "X"
            AI = "O"
            inputUnderstood = True
        elif starting == "N":
            user = "O"
            AI = "X"
            inputUnderstood = True
        else:
            starting = input("Could not understand your response. Please type Y or N. Do you want to start? ").upper()
        return user, AI



def main(position):
    print("\n")
    print("|__% s__|__% s__|__% s__|" % (position["(1,3)"], position["(2,3)"], position["(3,3)"]))
    print("|__% s__|__% s__|__% s__|" % (position["(1,2)"], position["(2,2)"], position["(3,2)"]))
    print("|__% s__|__% s__|__% s__|" % (position["(1,1)"], position["(2,1)"], position["(3,1)"]))
    print("\n")
    move = input("Which move would you like to make? ")
    currentPosition[move] = "X"



# User is always X and AI is always O
# Coordinates are top-right point of each square
# Each square has three states, Blank, AI, and User.
currentPosition = {
    "(1,1)": "",
    "(1,2)": "",
    "(1,3)": "",
    "(2,1)": "",
    "(2,2)": "",
    "(2,3)": "",
    "(3,1)": "",
    "(3,2)": "",
    "(3,3)": ""
}

startingPosition = {
    "(1,1)": "",
    "(1,2)": "",
    "(1,3)": "",
    "(2,1)": "",
    "(2,2)": "",
    "(2,3)": "",
    "(3,1)": "",
    "(3,2)": "",
    "(3,3)": ""
}


if __name__ == "__main__":
    main(startingPosition)