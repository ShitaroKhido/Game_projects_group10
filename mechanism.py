###########################################
##### COPYRIGHTS AND RESERVED BY KHID #####
###########################################
from random import randint
from tkinter import Canvas



##### ENEMY MODEL ######
class Enemy:
    """Enemy
    
    Enemy class containt:
    number_of_enemy(self, number:int)
    move_enemy(self)
    enem_dictionary(self)
    """
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
        print(self.VOLOCITY)


class Player:
    
    PLAYER_MOVE_SPEED = 40

    def __init__(self,canvas, player_canvas):
        self._canvas = canvas
        self._player = player_canvas
    
    def player_movements(self, x, y):
        self._canvas.move(self._player, x, y)

    def move_right(self):
        self.player_movements(x = self.PLAYER_MOVE_SPEED)

    def move_left(self):
        self.player_movements(x = -self.PLAYER_MOVE_SPEED)

    def move_down(self):
        self.player_movements(y = self.PLAYER_MOVE_SPEED)

    def move_up(self):
        self.player_movements(y = -self.PLAYER_MOVE_SPEED)

