from engine import Board


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
    print(" % s  |  % s  |  % s  " % (position[6], position[7], position[8]))
    print("________________")
    print(" % s  |  % s  |  % s  " % (position[3], position[4], position[7]))
    print("________________")
    print(" % s  |  % s  |  % s  " % (position[0], position[1], position[2]))
    print("________________")
    move = input("Which move would you like to make? ")





if __name__ == "__main__":
    starting()