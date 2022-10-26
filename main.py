from tkinter import Button, Frame, PhotoImage, Tk, Canvas, mainloop, BOTH


### CONSTANT
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_TITLE = "THE CORAVID"

GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"
CROSSHAIR = "Game_projects_group10\\assets\image\crosshairs.png"

class Player:
    
    def __init__(self, master, canvas, position, player_img, player_crosshair) -> None:
        self._canvas = canvas
        self._player = self._canvas.create_image(position, image = player_img, tag="player")
        self._player_crosshair = self._canvas.create_image(position, image = player_crosshair)
        self._master = master

        self._master.bind("<w>", self.move_up)
        self._master.bind("<a>", self.move_left)
        self._master.bind("<s>", self.move_down)
        self._master.bind("<d>", self.move_right)
        self._master.bind("<Motion>", self.player_crosshair)


    def player_crosshair(self, event):
        self._canvas.moveto(self._player_crosshair, event.x-40, event.y-40)
    


class Home:
    

    def __init__(self,master, canvas, background_location) -> None:
        self.background = PhotoImage(file= background_location)
        self.add_background = canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=self.background)



#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    main_canvas = Canvas(root)
    main_canvas.pack(expand=True, fill=BOTH)

    player_img = PhotoImage(file=CHARACTER_IMG_LOCATION)
    player_crosshair = PhotoImage(file=CROSSHAIR)
    
    player  = Player(root, main_canvas, [100,100], player_img, player_crosshair )

    mainloop()
