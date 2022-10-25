from tkinter import *

class Player:
    
    PLAYER_POSITION = [10,10,120,120]

    def __init__(self, master) -> None:
        Canvas().__init__(master)
        self._player_img = PhotoImage(file="Game_projects_group10/assets/image/virus2.png")
        self._crosshair_img = PhotoImage(file="Game_projects_group10/assets/image/crosshairs.png")
        self._canvas = Canvas(master)
        self._canvas.pack(expand=True, fill=BOTH)
        self._player = self._canvas.create_image(10, 10 , image=self._player_img)
        self._crosshair = self._canvas.create_image(
            self._canvas.coords(self._player)[0]+20,
            self._canvas.coords(self._player)[1]+20,
            image=self._crosshair_img
        )
        self._master = master
        ### MOVEMENTS KEY
        self._master.bind("<w>", self.up)
        self._master.bind("<a>", self.left)
        self._master.bind("<s>", self.down)
        self._master.bind("<d>", self.right)
        ### AIMING MOTION
        self._master.bind("<Motion>", self._player_crosshair)

    def _player_crosshair(self, event):
        self._canvas.delete(self._crosshair)
        self._crosshair = self._canvas.create_image(
            event.x,
            event.y,
            image=self._crosshair_img
        )
        print(f"{event.x} {event.y}")

    def movements(self, x,y):
        self._canvas.move(self._player, x, y)

    
    def right(self, event):
        self.movements(20, 0)

    def left(self, event):
        self.movements(-20, 0)

    def up(self, event):
        self.movements(0, -20)

    def down(self, event):
        self.movements(0, 20)

########################################################################################


if __name__=="__main__":

    root = Tk()
    root.geometry("1000x600")
    root.resizable(0,0)
    
    player = Player(root)

    mainloop()