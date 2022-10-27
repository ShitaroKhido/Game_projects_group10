###########################################
##### COPYRIGHTS AND RESERVED BY KHID #####
###########################################
from tkinter import Canvas

class Character:
    
    def __init__(self, master_window, main_canvas, player_canvas):
        self._master = master_window
        self._canvas = main_canvas
        self._player = player_canvas
        #### PLAYER COORDINATION
        self._coord = self._canvas.coords(self._player)

    def get_coord(self):
        return self._coord


class Movements(Character):
    
    MOVES_VOLOCITY = 20
    PLATFORM_SIZE = [1000, 600]
    def __init__(self, master_window, main_canvas, player_canvas):
        super().__init__(master_window, main_canvas, player_canvas)
        
    def check_if_wall(self):
        x = self._coord[0] + self._coord[2] / 2
        y = self._coord[1] + self._coord[3] / 2
        player_coord = [x, y]
        
        if player_coord[0] >= self.PLATFORM_SIZE[0]:
            move = False
        elif player_coord[1] >= self.PLATFORM_SIZE[1]:
            move = False
        else:
            move = True
        return move
    
    def move_character(self, x=0, y=0):
        return self._canvas.move(self._player, x, y)

    def move_right(self, event):
        if self.check_if_wall:
            self.move_character(x = self.MOVES_VOLOCITY)
    
    def move_left(self, event):
        if self.check_if_wall:
            self.move_character( x = -(self.MOVES_VOLOCITY))
    
    def move_up(self, event):
        if self.check_if_wall:
            self.move_character( y = -(self.MOVES_VOLOCITY))

    def move_down(self, event):
        if self.check_if_wall:
            self.move_character( y = self.MOVES_VOLOCITY)
    