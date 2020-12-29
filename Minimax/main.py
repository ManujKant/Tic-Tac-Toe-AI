import random

class Board:

    def __init__(self, position, AI, user):
        self.position = position
        # AI is just X or O
        self.AI = AI
        self.user = user

    
    def emptyBoxes(self, position):

        emptyBoxes = []
        count = -1
        for box in position:
            count += 1
            if box == " ":
                emptyBoxes.append(count)

        return emptyBoxes
    
    def findPossibilities(self, position, value):

        emptyBoxes = self.emptyBoxes(position)

        possibilities = []

        for index in emptyBoxes:
            position[index] = f"{value}"
            possibilities.append(position[:])
            position[index] = " "

        return possibilities

    def evaluatePosition(self, position):
        # rows
        for i in range(0, 7, 3):
            if position[i] == position[i+1]:
                if position [i] == position[i+2]:
                    if position[i] == " ":
                        pass
                    elif position[i] == self.user:
                        return -1
                    elif position[i] == self.AI:
                        return 1
        # columns
        for i in range(3):
            if position[i] == position[i+3]:
                if position[i] == position[i+6]:
                    if position[i] == " ":
                        pass
                    elif position[i] == self.user:
                        return -1
                    elif position[i] == self.AI:
                        return 1
        # diagonals

        if position[0] == position[4]:
            if position[0] == position[8]:
                if position[0] == " ":
                    pass
                elif position[0] == self.user:
                    return -1
                elif position[0] == self.AI:
                    return 1
        
        if position[2] == position[4]:
            if position[2] == position[6]:
                if position[2] == " ":
                    pass
                elif position[2] == self.user:
                    return -1
                elif position[2] == self.AI:
                    return 1
        if self.emptyBoxes(position) == []:
            return 0

        
        return None
        
    def minimaxAlgorithm(self, position, maximizing):
        if self.evaluatePosition(position) != None:
            return self.evaluatePosition(position)
            
        if maximizing == True:
            evaluations = []
            for possibility in self.findPossibilities(position, self.AI):
                evaluation = self.minimaxAlgorithm(possibility, False)
                evaluations.append(evaluation)
            return max(evaluations)

        else:
            evaluations = []
            for possibility in self.findPossibilities(position, self.user):
                evaluation = self.minimaxAlgorithm(possibility, True)
                evaluations.append(evaluation)
            return min(evaluations)
            

    def bestMove(self):
        if self.evaluatePosition(self.position) == None:
            bestMove = []

            for position in self.findPossibilities(self.position, self.AI):
                evaluation = self.minimaxAlgorithm(position, False)
                position.append(evaluation)
                bestMove.append(position)
            
            wins = [i for i in bestMove if i[-1] == 1]
            draws = [i for i in bestMove if i[-1] == 0]
            losses = [i for i in bestMove if i[-1] == -1]

            if len(wins) != 0:
                finalMove =  random.choice(wins)
                return finalMove
            
            elif len(draws) != 0:
                finalMove =  random.choice(draws)
                return finalMove
            
            elif len(losses) != 0:
                finalMove =  random.choice(losses)
                return finalMove

        else:
            result = self.evaluatePosition(self.position)
            return result



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
 


def X(position):


    move = Board(position, AI, user)
    if move.evaluatePosition(position) != None:
        print("\n")
        print(" % s  |  % s  |  % s  " % (position[6], position[7], position[8]))
        print("_______________")
        print(" % s  |  % s  |  % s  " % (position[3], position[4], position[5]))
        print("_______________")
        print(" % s  |  % s  |  % s  " % (position[0], position[1], position[2]))
        
        if move.evaluatePosition(position) == 1:
            print("\n")
            print("I WIN")
            print("\n")
        if move.evaluatePosition(position) == 0:
            print("\n")
            print("Draw")
            print("\n")
        if move.evaluatePosition(position) == -1:
            print("\n")
            print("Good Job")
            print("\n")
  

    if move.evaluatePosition(position) == None:
        newPosition = move.bestMove()
        eval = move.evaluatePosition(newPosition)
        
        print("\n")
        print(" % s  |  % s  |  % s  " % (newPosition[6], newPosition[7], newPosition[8]))
        print("_______________")
        print(" % s  |  % s  |  % s  " % (newPosition[3], newPosition[4], newPosition[5]))
        print("_______________")
        print(" % s  |  % s  |  % s  " % (newPosition[0], newPosition[1], newPosition[2]))

        if eval == 1:
            print("\n")
            print("I WIN")
            print("\n")
        elif eval == 0:
            print("\n")
            print("Draw")
            print("\n")
        elif eval== -1:
            print("\n")
            print("Good Job")
            print("\n")
        

        if eval == None:
            inputUnderstood = False
            while inputUnderstood == False:
                move = input("Which move would you like to make? ")
                if int(move) - 1 not in [0,1,2,3,4,5,6,7,8]:
                    print("That square is out of range, pick another square. (1-9)")
                elif newPosition[int(move)-1] == " ":
                    newPosition[int(move)-1] = user
                    inputUnderstood = True
                else:
                    print("That square is taken, pick another square. (1-9)")
            X(newPosition)

def O():
    
    startingPosition = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    print("\n")
    print("    |     |     ")
    print("_______________")
    print("    |     |     ")
    print("_______________")
    print("    |     |     ")
    print("\n")

    inputUnderstood = False
    while inputUnderstood == False:
        move = input("Which move would you like to make? ")
        if int(move) - 1 not in [0,1,2,3,4,5,6,7,8]:
                    print("Move not in range")
        else:
            inputUnderstood = True
    startingPosition[int(move) - 1] = user


    X(startingPosition)


if AI == "X":
    X([" ", " ", " ", " ", " ", " ", " ", " ", " "])
else:
    O()