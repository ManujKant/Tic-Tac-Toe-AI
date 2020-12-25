class Board:

    def __init__(self, position, AI, user):
        self.position = position
        # AI is just X or O
        self.AI = AI
        self.user = user
    

    def engine(self):

        position = self.position
        AI = self.AI
        user = self.user

        
    def tree(postion, emptyBoxes):
        position = self.position
        emptyBoxes = []
        count = -1
        for box in position:
            count += 1
            if box == " ":
                emptyBoxes.append(count)

        




        
        
        

            

position = [" ", " ", " ", "X", "X", "O", "X", "O", " "]


Board(position, "O", "X").engine()


