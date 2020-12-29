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
        bestMove = []
        eval = -2
        for position in self.findPossibilities(self.position, self.AI):
            evaluation = self.minimaxAlgorithm(position, True)
            if evaluation > eval:
                eval = evaluation
                bestMove = position
        
        return bestMove