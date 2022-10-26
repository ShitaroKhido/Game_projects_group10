from tkinter import PhotoImage, Tk, Canvas, mainloop, BOTH


### CONSTANT
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_TITLE = "THE CORAVID"

GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"

class Player:
    
    def __init__(self, master, canvas, position, player_img) -> None:
        self._canvas = canvas
        self._player = self._canvas.create_image(position, image = player_img)
        self._master = master
    

    def movement(self, x = 0, y = 0):
        self._canvas.move(self._player, x, y)
    
    def move_left(self):
        self.movement(x =- 10)
    
    def move_right(self):
        self.movement(x = 10)
    
    def move_up(self):
        self.movement(y = -10)
    
    def move_down(self):
        self.movement(y = 10)
    




#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")


    mainloop()
