###########################################
##### COPYRIGHTS AND RESERVED BY KHID #####
###########################################
from random import randint
from tkinter import Canvas

##### CHARACTER MODEL ######
class Character:
    
    def __init__(self, master_window, main_canvas, player_canvas):
        self._master = master_window
        self._canvas = main_canvas
        self._player = player_canvas
        #### PLAYER COORDINATION
        self._coord = self._canvas.coords(self._player)
        self._crosshair = None

    def get_coord(self):
        return self._coord

    def aim(self, event):
        self._canvas.moveto(self._crosshair, event.x-40, event.y-40)

    def crosshair(self, crosshair_image):
        self._crosshair = self._canvas.create_image(self._coord[0], self._coord[0], image=crosshair_image)

    def shoot(self, bullet_img):
        pass
        

class Movements(Character):
    
    MOVES_VOLOCITY = 60
    PLATFORM_SIZE = [1000, 600]

    def __init__(self, master_window, main_canvas, player_canvas):
        super().__init__(master_window, main_canvas, player_canvas)

    def move_character(self, x=0, y=0):
        self._canvas.move(self._player, x, y)

    def move_right(self, event):
        self.move_character(x = self.MOVES_VOLOCITY)
    
    def move_left(self, event):
        self.move_character( x = -(self.MOVES_VOLOCITY))
    
    def move_up(self, event):
        self.move_character( y = -(self.MOVES_VOLOCITY))

    def move_down(self, event):
        self.move_character( y = self.MOVES_VOLOCITY)


class Enemy:
    
    VOLOCITY = {}
    DICT_OF_ENEMY = {}

    def __init__(self,master_window, main_canvas, enemy_img):
        self._master = master_window
        self._canvas = main_canvas
        self._enemy_img = enemy_img

    def number_of_enemy(self, number:int):
        for i in range(number):
            # self._canvas.create_image(randint(0,900), randint(0,500), image=self._enemy_img)
            key = f"enemy_{i+1}"
            self.DICT_OF_ENEMY[key] = self._canvas.create_image(randint(0,900), randint(0,500), image=self._enemy_img)

        for key in self.DICT_OF_ENEMY:
            self.VOLOCITY[key] = {"x":randint(1,10) , "y":randint(1,10)}

    def move_enemy(self):

        for key in self.DICT_OF_ENEMY:

            if self._canvas.coords(self.DICT_OF_ENEMY[key])[0] >= 1000:
                self.VOLOCITY[key]["x"] = -self.VOLOCITY[key]["x"]

            elif self._canvas.coords(self.DICT_OF_ENEMY[key])[1] >= 600:
                self.VOLOCITY[key]["y"] = -self.VOLOCITY[key]["y"]

            elif self._canvas.coords(self.DICT_OF_ENEMY[key])[0] <= 0:
                self.VOLOCITY[key]["x"] = -1*self.VOLOCITY[key]["x"]

            elif self._canvas.coords(self.DICT_OF_ENEMY[key])[1] <= 0:
                self.VOLOCITY[key]["y"] = -1*self.VOLOCITY[key]["y"]

            self._canvas.move(self.DICT_OF_ENEMY[key], self.VOLOCITY[key]["x"], self.VOLOCITY[key]["y"])
        
        self._canvas.after(40, self.move_enemy)

    def enem_dictionary(self):
        print(self.DICT_OF_ENEMY)
        print(self.VOLOCITY)