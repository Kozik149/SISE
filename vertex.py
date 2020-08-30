

class Vertex:
    columns_number = None
    rows_number = None
    size = None
    parent = None
    moveLetter = ""
    depth = None
    game = []
    emptyTile = 0

    def __init__(self, *args):
        if len(args) == 1:
            self.rows_number = args[0][0]
            self.columns_number = args[0][1]
            self.size = self.rows_number * self.columns_number
            self.depth = 0
            self.game = [None] * self.size
            self.game[0: 0+len(self.game)] = args[0][2: 2+len(self.game)]
            self.children = []
        else:
            self.rows_number = args[1]
            self.columns_number = args[2]
            self.size = self.rows_number * self.columns_number
            self.game = [x for x in args[0]]
            self.children = []

    def move(self, g = [], i1 = None, i2 = None, letter = ""): # TODO children can not be mutable
        new_board = [x for x in g]
        tmp = new_board[i1]
        new_board[i1] = new_board[i2]
        new_board[i2] = tmp
        child = Vertex(new_board, self.columns_number, self.rows_number)
        child.moveLetter = letter
        child.parent = self
        child.depth = self.depth + 1
        self.children.append(child)

    def make_children(self, *args):
        if len(args) == 0:
            for x in range(len(self.game)):
                if (self.game[x] == 0):
                    empty_tile = x
            self.moveUp(self.game, empty_tile)
            self.moveDown(self.game, empty_tile)
            self.moveRight(self.game, empty_tile)
            self.moveLeft(self.game, empty_tile)
        else:
            for x in range(len(self.game)):
                if (self.game[x] == 0):
                    empty_tile = x

            for order in args[0]:
                if (order == 'L'):
                    self.moveLeft(self.game, empty_tile)
                elif (order == 'R'):
                    self.moveRight(self.game, empty_tile)
                elif (order == 'U'):
                    self.moveUp(self.game, empty_tile)
                elif (order == 'D'):
                    self.moveDown(self.game, empty_tile)
                else:
                    print("Wrong order!")

    def moveUp(self, g = [], index = None):
        if (index - self.columns_number >= 0):
            self.move(g, index - self.columns_number, index, "U")

    def moveDown(self, g = [], index = None):
        if (index < len(self.game) - self.columns_number):
            self.move(g, index + self.columns_number, index, "D")

    def moveLeft(self, g = [], index = None):
        if (index % self.columns_number > 0):
            self.move(g, index - 1, index, "L")

    def moveRight(self, g = [], index = None):
        if (index % self.columns_number < self.columns_number - 1):
            self.move(g, index + 1, index, "R")

    def goalCheck(self):
        isBoardGoal = True
        tileValue = self.game[0]
        for i in range(1, len(self.game) - 1, 1):
            if (tileValue > self.game[i]):
                isBoardGoal = False
            tileValue = self.game[i]
        return isBoardGoal

    def calculateHammingDistance(self):
        distance = 0
        for i in range(1, len(self.game), 1):
            if (self.game[i] != 0 & self.game[i] != i + 1):
                distance += 1
        return distance + self.depth

    def calculateManhattanDistance(self):
        distance = 0
        for i in range(len(self.game)):
            if (self.game[i] != 0 & self.game[i] != i + 1):
                CorrectX = (self.game[i] - 1) % self.columns_number
                CorrectY = (self.game[i] - 1) / self.rows_number
                IncorrectX = i % self.columns_number
                IncorrectY = i / self.rows_number
                distance += abs(CorrectX - IncorrectX) + abs(CorrectY - IncorrectY)
        return distance + self.depth