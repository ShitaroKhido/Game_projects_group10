from tkinter import *

class Player:
    
    PLAYER_POSITION = [100,100,120,120]

    def __init__(self, master) -> None:
        Canvas().__init__(master)
        self._canvas = Canvas(master)
        self._canvas.pack(expand=True, fill=BOTH)
        self._player = self._canvas.create_oval(Player.PLAYER_POSITION)
        self._master = master

        self._master.bind("<w>", self.up)
        self._master.bind("<a>", self.left)
        self._master.bind("<s>", self.down)
        self._master.bind("<d>", self.right)

    def movements(self, x,y):
        self._canvas.move(self._player, x, y)

    def right(self, event):
        self.movements(10, 0)

    def left(self, event):
        self.movements(-10, 0)

    def up(self, event):
        self.movements(0, -10)

    def down(self, event):
        self.movements(0, 10)

def show(event):
    global line
    print(f"{event.x} {event.y}")




if __name__=="__main__":
    root = Tk()
    root.geometry("1000x600")
    root.resizable(0,0)

    player = Player(root)
    root.bind("<Motion>", show)

    mainloop()