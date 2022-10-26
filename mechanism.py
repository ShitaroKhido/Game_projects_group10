#######################################
### COPYRIGHTS AND RESERVED BY KHID ###
#######################################

from tkinter import Button, Frame, PhotoImage, Tk, Canvas, mainloop, BOTH


class Character:

    """Character model


    This is the character class which container the method:

    CHARACTER COORDINATION:
    def player_coord(self)

    DIRECITON MOVEMENTS:
    self.move_right(self, event)
    self.move_left(self, event)
    self.move_up(self, event)
    self.move_down(self, event)
    """

    def __init__(self, main_canvas, player):
        Canvas().__init__()
        self._player =  player
        self._canvas = main_canvas

    def player_coord(self):
        return self._canvas.coords(self._player)

    def movements(self,  x=0 , y=0):
        self._canvas.move(self._player, x, y)

    def move_right(self, event):
        self.movements(60, 0)

    def move_left(self, event):
        self.movements(-60, 0)
    
    def move_up(self, event):
        self.movements(0, -60)
    
    def move_down(self, event):
        self.movements(0, 60,)

    

class Gun:

    """Gun

    Is the model item for charcter.
    METHOD:
    projectile(self, event)
    shoot(self, event)
    """
    
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
        ### VECTORS CALCULATION
        vector_a = (self.x1+self.x2) / 2
        vector_b = (self.y1+self.y2) / 2
        ### PLAYER COORDINATION POINT
        player_x = event.x - vector_a
        player_y = event.y - vector_b
        ### VOLOCITY OF DIRECTION
        x_direction = (player_x + 2) - (player_x - 2) / self.AIM_ALIGNMENT
        y_direction = (player_y + 2) - (player_y - 2) / self.AIM_ALIGNMENT

        return [x_direction, y_direction]

    def shoot(self, event):
        direction = self.projectile(event)
        self._canvas.move(None, direction[0], direction[1])

