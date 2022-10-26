from tkinter import Button, Frame, PhotoImage, Tk, Canvas, mainloop, BOTH


### CONSTANT
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_TITLE = "THE CORAVID"

GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"
CROSSHAIR = "Game_projects_group10\\assets\image\crosshairs.png"


class Character:
    
    def __init__(self, main_canvas, player):
        Canvas().__init__()
        self._player =  player
        self._canvas = main_canvas

    def player_coord(self):
        return self._canvas.coords(self._player)

    def movements(self, x = 0 , y = 0):
        self._canvas.move(self._player, x, y)

    def move_right(self, event):
        self.movements(event, x = 60)

    def move_left(self, event):
        self.movements(event, x = -60)
    
    def move_up(self, event):
        self.movements(event, y = -60)
    
    def move_down(self, event):
        self.movements(event, y = 60)


#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    main_canvas = Canvas(root,)
    main_canvas.pack(expand=True, fill=BOTH)
    # root.bind("<Button-1>", click)
    mainloop()
