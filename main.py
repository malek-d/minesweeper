import os, sys,field
from random import randint

# Global constants
player_field = ""
FIELD_WIDTH = 40
ROWS = 20
COLUMNS = 24
MAX_MINES = 99

def setup():
    size(FIELD_WIDTH * COLUMNS, FIELD_WIDTH * ROWS)
    global player_field
    player_field = field.Field(COLUMNS, ROWS, MAX_MINES)
    #player_field.printField()
def draw():
    y = 0
    for row in player_field.field:
        x = 0
        for column in row:
            if column.isFlagged:
                textSize(38)
                fill(0, 102, 153, 204);
                text("F", x + 10, y + FIELD_WIDTH - 5)
                fill(0, 102, 153, 0);
            elif column.isClicked:
                if column.bomb:
                    textSize(38)
                    fill(255,0,0,204)
                    text("X", x + 10, y + FIELD_WIDTH - 5)
                    fill(255,0,0,0)
                elif column.label != None and column.label != "X":
                    textSize(38)
                    fill(0,0, 0, 204);
                    text(str(column.label), x + 10, y + FIELD_WIDTH - 5)
                    fill(0, 102, 153, 0);
                else:
                    fill(255)
                rect(x,y,FIELD_WIDTH,FIELD_WIDTH, 2) 
            else:   
                fill(220,220,220)
                rect(x,y,FIELD_WIDTH,FIELD_WIDTH, 2)
            x += FIELD_WIDTH
        y += FIELD_WIDTH
def keyPressed():
    if key == ' ':
       global player_field
       player_field = field.Field(COLUMNS, ROWS, MAX_MINES)
       redraw()
def mousePressed():
    x_index = mouseX / FIELD_WIDTH
    y_index = mouseY / FIELD_WIDTH
    true_x = x_index * FIELD_WIDTH
    true_y = y_index * FIELD_WIDTH
    global player_field
    if player_field.gameOver:
        player_field = field.Field(COLUMNS, ROWS, MAX_MINES)
        redraw()
    if mouseButton == LEFT:
        player_field.search(x_index, y_index)
    if mouseButton == RIGHT:
        player_field.setFlag(x_index,y_index)
    print("[{0},{1}] = {2}".format(x_index,y_index, player_field.field[y_index][x_index].label))
    
