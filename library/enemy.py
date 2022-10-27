###########################################
##### COPYRIGHTS AND RESERVED BY KHID #####
###########################################
from random import randint
from tkinter import Canvas

class Enemy:

    """Enemy

    Enemy class containt:
    number_of_enemy(self, number:int)
    move_enemy(self)
    enem_dictionary(self)
    """

    volocity = {}
    DICT_OF_ENEMY = {}

    def __init__(self, master_window, main_canvas, enemy_img):
        self._master = master_window
        self._canvas = main_canvas
        self._enemy_img = enemy_img

    def number_of_enemy(self, number: int):
        for i in range(number):
            # self._canvas.create_image(randint(0,900), randint(0,500), image=self._enemy_img)
            key = f"enemy_{i+1}"
            self.DICT_OF_ENEMY[key] = self._canvas.create_image(
                randint(0, 900), randint(0, 500), image=self._enemy_img)

        for key in self.DICT_OF_ENEMY:
            self.volocity[key] = {"x": randint(1, 10), "y": randint(1, 10)}

    def move_enemy(self):

        for key in self.DICT_OF_ENEMY:

            if self._canvas.coords(self.DICT_OF_ENEMY[key])[0] >= 1000:
                self.volocity[key]["x"] = -self.volocity[key]["x"]

            elif self._canvas.coords(self.DICT_OF_ENEMY[key])[1] >= 600:
                self.volocity[key]["y"] = -self.volocity[key]["y"]

            elif self._canvas.coords(self.DICT_OF_ENEMY[key])[0] <= 0:
                self.volocity[key]["x"] = -1*self.volocity[key]["x"]

            elif self._canvas.coords(self.DICT_OF_ENEMY[key])[1] <= 0:
                self.volocity[key]["y"] = -1*self.volocity[key]["y"]

            self._canvas.move(
                self.DICT_OF_ENEMY[key], self.volocity[key]["x"], self.volocity[key]["y"])

        self._canvas.after(40, self.move_enemy)

    def enem_dictionary(self):
        print(self.DICT_OF_ENEMY)
        print(self.volocity)
        print(self.volocity)
