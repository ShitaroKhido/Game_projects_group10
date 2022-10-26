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


class Gun:
    
    AIM_ALIGNMENT = 12

    def __init__(self, canvas, player) -> None:
        self._player = player
        self._canvas = canvas
        self._player_coord = self._canvas.coords(self._player)
        self.x1 = self._player_coord[0]
        self.y1 = self._player_coord[1]
        self.x2 = self._player_coord[2]
        self.y2 = self._player_coord[3]

    def projectile(self, event):
        vector_a = (self.x1+self.x2) / 2
        vector_b = (self.y1+self.y2) / 2

        player_x = event.x - vector_a
        player_y = event.y - vector_b

        x_direction = (player_x + 2) - (player_x - 2) / self.AIM_ALIGNMENT
        y_direction = (player_y + 2) - (player_y - 2) / self.AIM_ALIGNMENT

        return [x_direction, y_direction]


    def shoot(self, event):
        direction = self.projectile(event)
        self._canvas.move(None, direction[0], direction[1])

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
