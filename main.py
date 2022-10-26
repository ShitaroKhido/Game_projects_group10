from tkinter import Frame, PhotoImage, Tk, Canvas, mainloop, BOTH


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

        self._master.bind("<w>", self.move_up)
        self._master.bind("<a>", self.move_left)
        self._master.bind("<s>", self.move_down)
        self._master.bind("<d>", self.move_right)
    def movement(self, x = 0, y = 0):
        self._canvas.move(self._player, x, y)
    
    def move_left(self, event):
        self.movement(x =- 10)
    
    def move_right(self, event):
        self.movement(x = 10)
    
    def move_up(self, event):
        self.movement(y = -10)
    
    def move_down(self, event):
        self.movement(y = 10)
    




#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    ### MAIN GAME FRAME

    level_selection = Frame(root)
    frame_level_1 = Frame(root)
    frame_level_2 = Frame(root)
    frame_level_3 = Frame(root)

    # level_selection.pack(expand=True, fill=BOTH)
    frame_level_1.pack(expand=True, fill=BOTH)
    # frame_level_2.pack(expand=True, fill=BOTH)
    # frame_level_3.pack(expand=True, fill=BOTH)
    ### MAIN CANVAS
    canvas = Canvas(frame_level_1)
    canvas.pack(expand=True, fill=BOTH)
    ### PLAYER IMAGES
    player_img = PhotoImage(file=CHARACTER_IMG_LOCATION)

    main_player = Player(frame_level_1, canvas, [100,100], player_img)


    mainloop()
