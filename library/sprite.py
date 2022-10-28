from random import randint
from .constant import WINDOW_HEIGHT, WINDOW_WIDTH


class Generate_sprite:

    def __init__(self, dictionary=None, img=None):
        self._dict = dictionary
        self._img  = img


class MakeEnemy(Generate_sprite):
    
    def __init__(self, emtpy_dictionary=None, enemy_img=None):
        super().__init__(emtpy_dictionary, enemy_img)
        self._dict = emtpy_dictionary
        self._img  = enemy_img
    
    def create_enemy_data(self, count):
        for i in range(count):
            key = f"enemy_{i+1}"
            rand_y = randint(1, WINDOW_HEIGHT-100)
            rand_x = randint(1, WINDOW_WIDTH-100)

            vol_x = randint(1,10)
            vol_y = randint(1,10)

            self._dict[key] = {
                "position": [rand_x, rand_y],
                "volocity": [vol_x, vol_y],
                "img_location": self._img
            }


class Items(Generate_sprite):
    
    def __init__(self, empty_dictionary=None, list_img=None):
        super().__init__(empty_dictionary, list_img)
        self._dict = empty_dictionary
        self._img_list  = list_img
    
    def generate_item_dict(self, count):
        for i in range(count):
            key = f"item_{i+1}"

            rand_y = randint(1, WINDOW_HEIGHT-100)
            rand_x = randint(1, WINDOW_WIDTH-100)
            
            imgs = self._img_list[randint(0,len(self._img_list)-1)]

            self._dict[key] = {
                "position": [rand_x, rand_y],
                "img_location": imgs
            }



