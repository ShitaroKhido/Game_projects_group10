from tkinter import Tk, Canvas, mainloop, BOTH


### CONSTANT
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600


GAME_TITLE = "THE CORAVID"
GMAE_ICON_LOCATION = ""






class Character:
    
    def __init__(self, canvas) -> None:
        pass


class Draw:
    
    def __init__(self, canvas, grid, x, y, grid_size):
        self.canvas = canvas
        self.grid = grid
        self.grid_size = grid_size
        self.x = x
        self.y = y

    def level(self):
        pass




#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")


    root.mainloop()