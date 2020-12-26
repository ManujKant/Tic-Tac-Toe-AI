class Board:

    def __init__(self, position, AI, user):
        self.position = position
        # AI is just X or O
        self.AI = AI
        self.user = user

    
    def emptyBoxes(self, position):

        emptyBoxes = []
        count = -1
        for box in self.position:
            count += 1
            if box == " ":
                emptyBoxes.append(count)

        return emptyBoxes
    
    def findPossiblities(self, position):

        emptyBoxes = self.emptyBoxes(position)

        possibilities = []

        for index in emptyBoxes:
            self.position[index] = f"{self.AI}"
            possibilities.append(self.position[:])
            self.position[index] = " "

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
        
        
    def createTree(self):
        
        possibilityTree = []
        possibilityTree.append(self.position)
        for i in range(len(self.emptyBoxes(positions))):
            temp = []
            for x in possibilityTree[-1]:
                temp.append(self.findPossiblities(x))
            possibilityTree.append(temp)
           

            




# the ops are o



position = [" ", "X", " ", "O", "O", "O", " ", "X", " "]
Board = Board(position, "X", "O")
Board.createTree()


