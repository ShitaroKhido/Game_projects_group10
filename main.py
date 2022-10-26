from tkinter import PhotoImage, Tk, Canvas, mainloop, BOTH


### CONSTANT
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600


GAME_TITLE = "THE CORAVID"
GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"




### Khid
class Character:
    
    CANVAS_TIMING = 10

    def __init__(self,master, canvas, player_image, xPos, yPos):
        self._canvas = canvas
        self._player = self._canvas.create_image(xPos, yPos, image=player_image)
        self._master = master
        ### KEY BINDING FOR THE PLAYERS
        self._master.bind("<w>", self.move_up)
        self._master.bind("<a>", self.move_left)
        self._master.bind("<s>", self.move_down)
        self._master.bind("<d>", self.move_right)
    
    ### MOVEMENTS METHOD FOR THE CHARACTER
    def _movement(self,event, xValue = 0, yValue = 0):
        self._canvas.move(self._player, xValue, yValue)
        self._canvas.after(self.CANVAS_TIMING, lambda:self._movement(event))

    def move_left(self, event):
        self._movement(event,xValue=-10)
    
    def move_right(self, event):
        self._movement(event,xValue=10)

    def move_up(self, event):
        self._movement(event,yValue=-10)
    
    def move_down(self, event):
        self._movement(event,yValue=10)


class Virus:

    VIRUS_SPEED = 10
    VOLOCITY = {
        "xVolocity": 10,
        "yVolocity": 10
    }

    def __init__(self, master, canvas, virus_image, xPos, yPos):
        self._master = master
        self._canvas = canvas
        self._virus_img = virus_image
        self._virus = self._canvas.create_image(xPos, yPos, image=self._virus_img)

    def _movement(self):
        virus_coordination = self._canvas.coords(self._virus)
        if virus_coordination[0] >= WINDOW_WIDTH:
            self.VOLOCITY["xVolocity"] = -(self.VOLOCITY["xVolocity"])
        if virus_coordination[1] >= WINDOW_HEIGHT:
            self.VOLOCITY["yVolocity"] = -(self.VOLOCITY["yVolocity"])
        if virus_coordination[0] == 0:
            self.VOLOCITY["xVolocity"] = -1*(self.VOLOCITY["xVolocity"])
        if virus_coordination[1] == 0:
            self.VOLOCITY["yVolocity"] = -1*(self.VOLOCITY["yVolocity"])
        ### MOVEMENTS PROCESS
        self._canvas.move(self._virus, self.VOLOCITY["xVolocity"], self.VOLOCITY["yVolocity"])
        self._canvas.after(self.VIRUS_SPEED,self._movement)
        




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

    gird=Draw()

    mainloop()