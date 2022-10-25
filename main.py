from tkinter import *

class Player:
    
    PLAYER_POSITION = [10,10,120,120]

    def __init__(self, master) -> None:
        Canvas().__init__(master)
        self._player_img = PhotoImage(file="Game_projects_group10/assets/image/virus2.png")
        self._canvas = Canvas(master)
        self._canvas.pack(expand=True, fill=BOTH)
        self._player = self._canvas.create_image(10, 10 , image=self._player_img)
        self._laser = self._canvas.create_line(
            self._canvas.coords(self._player)[0],
            self._canvas.coords(self._player)[1],
            self._canvas.coords(self._player)[0]+20,
            self._canvas.coords(self._player)[1]+20,
        )
        self._master = master
        ### MOVEMENTS KEY
        self._master.bind("<w>", self.up)
        self._master.bind("<a>", self.left)
        self._master.bind("<s>", self.down)
        self._master.bind("<d>", self.right)
        ### AIMING MOTION
        self._master.bind("<Motion>", self._show)

    def movements(self, x,y):
        self._canvas.move(self._player, x, y)

    def _show(self, event):
        self._canvas.delete(self._laser)
        self._laser = self._canvas.create_line(
            self._canvas.coords(self._player)[0],
            self._canvas.coords(self._player)[1],
            event.x,
            event.y,
        )
        print(f"{event.x} {event.y}")

    def right(self, event):
        self.movements(10, 0)

    def left(self, event):
        self.movements(-10, 0)

    def up(self, event):
        self.movements(0, -10)

    def down(self, event):
        self.movements(0, 10)








if __name__=="__main__":

    root = Tk()
    root.geometry("1000x600")
    root.resizable(0,0)

    
    player = Player(root)

    mainloop()