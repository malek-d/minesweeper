from random import randint
import tile

class Field:
    def __init__(self, columns, rows, max_bombs):
        self.columns = columns
        self.rows = rows
        self.max_bombs = max_bombs
        self.field = [ [ tile.Tile() for i in range(columns)] for n in range(rows) ]
        self.gameOver = False
        self.addMines()
        self.addNumbers()

    def addMines(self):
        for i in range(self.max_bombs):
            while True:
                x = randint(0, self.columns - 1)
                y = randint(0, self.rows - 1)
                if self.field[y][x].bomb == False:
                    self.field[y][x].bomb = True
                    break
   
    def setFlag(self,x,y):
        self.field[y][x].isFlagged = not self.field[y][x].isFlagged
    def printField(self):
        for row in self.field:
            row_string = "[ "
            for column in row:
                row_string += "{0}, ".format(column.bomb)
            print("{0}]".format(row_string))
            
    def addNumbers(self):
        for x in range(0, self.rows):
            for y in range(0,self.columns):
                bomb_adjacency = 0
                for (dx, dy) in [ (0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1) ]:
                    try:
                        if self.inBounds(x + dx, y+dy) and self.field[x+dx][y+dy].bomb:
                            bomb_adjacency += 1
                    except IndexError:
                        continue
                print("x:{0}/{1}; y{2}/{3}".format(x, self.columns - 1,y, self.rows - 1))
                if self.field[x][y].bomb:
                    self.field[x][y].label = "X"
                elif bomb_adjacency > 0:
                    self.field[x][y].label = bomb_adjacency
                    
    def inBounds(self, x,y):
        return x >= 0 and x < self.columns and y >= 0 and y < self.rows
    
    def setAllBombsToClicked(self):
        for x in range(0, self.rows):
            for y in range(0,self.columns):
                if self.field[x][y].bomb:
                    self.field[x][y].isClicked = True
    def search(self,x,y):    
        if not self.inBounds(x,y):
            return
        tile = self.field[y][x]
        if tile.isFlagged:
            return
        if tile.isClicked:
            return
        else:
            self.field[y][x].isClicked = True
        if tile.bomb:
            self.setAllBombsToClicked()
            self.gameOver = True
            return
        if tile.label != None and tile.label != "X":
            return
            
        for (dx, dy) in [ (0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1) ]:
            self.search(x + dx, y + dy)
