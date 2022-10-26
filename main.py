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

    def movements(self, event, x = 0 , y = 0):
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
    

    def __init__(self,player, gun, ammo) -> None:
        self._ammo_type = ammo
        self._gun_type = gun
        self._player = player

    def creat_bullet(self, event):
        p_coords = self.Canvas.coord(self._player)
        Canvas.create_image(event.x, event.y, )
# def click(event):
    
#     A = (main_canvas.coords(player)[0] + main_canvas.coords(player)[2]) /2
#     B = (main_canvas.coords(player)[1] + main_canvas.coords(player)[3]) /2
    
#     x_player = event.x - A
#     y_player = event.y - B

#     x_point = (x_player + 2) - (x_player - 2) / 12
#     y_point = (y_player + 2) - (y_player - 2) / 12

#     main_canvas.move(bullets, x_point, y_player)
#     main_canvas.after( 40, lambda:click(event))
    

#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    main_canvas = Canvas(root,)
    main_canvas.pack(expand=True, fill=BOTH)

    l1 = PhotoImage(file="Game_projects_group10\\assets\image\LEVEL1.png")

    Level_1 = main_canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=l1)

    character = PhotoImage(file=CHARACTER_IMG_LOCATION)
    player = main_canvas.create_oval(WINDOW_WIDTH/2-25, WINDOW_HEIGHT/2-25,WINDOW_WIDTH/2+25, WINDOW_HEIGHT/2+25)
    

    players = Character(main_canvas, player)
    root.bind("<w>", players.move_up)
    root.bind("<a>", players.move_left)
    root.bind("<s>", players.move_down)
    root.bind("<d>", players.move_right)
    # root.bind("<Button-1>", click)
    mainloop()
