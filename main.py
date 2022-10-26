from tkinter import Tk, Canvas, mainloop, BOTH
from turtle import position


### CONSTANT
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600


GAME_TITLE = "THE CORAVID"
GMAE_ICON_LOCATION = ""





### Khid
class Character:
    
    def __init__(self, canvas) -> None:
        pass










### SeangEng
class Draw:
    
    def __init__(self, canvas, grid, x, y, grid_size):
        self.canvas = canvas
        self.grid = grid
        self.grid_size = grid_size
        self.x = x
        self.y = y

    def level(self):
        brick=2
        man=1
        virus=3
        alcohol=4
        mask=5
        for row in self.canvas:
            for col in row:
                if col==brick:
                    pass
                elif col==man:
                    pass
                elif col==virus:
                    pass
                elif col==alcohol:
                    pass
                elif col==mask:
                    pass
                canvas.create_image(self.x,self.y,image="")

grid=[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    ]
position_x=0
position_y=0
grid_size=20



#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    canvas=Canvas(root)









    gird=Draw(canvas,grid,position_x,position_y,grid_size)

    root.mainloop()