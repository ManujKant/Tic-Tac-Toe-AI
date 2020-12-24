from classes import Board

def printBoard(position):
    print("\n")
    print("|__% s__|__% s__|__% s__|" % (position["(1,3)"], position["(2,3)"], position["(3,3)"]))
    print("|__% s__|__% s__|__% s__|" % (position["(1,2)"], position["(2,2)"], position["(3,2)"]))
    print("|__% s__|__% s__|__% s__|" % (position["(1,1)"], position["(2,1)"], position["(3,1)"]))
    print("\n")
    move = input("Which move would you like to make?))

# User is always X and AI is always O
# # Coordinates are top-right point of each square
# Each square has three states, Blank, AI, and User.
position = {
    "(1,1)": " ",
    "(1,2)": "O",
    "(1,3)": " ",
    "(2,1)": "X",
    "(2,2)": "O",
    "(2,3)": " ",
    "(3,1)": " ",
    "(3,2)": " ",
    "(3,3)": "X"
}

printBoard(position)