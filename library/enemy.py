from random import randint
from library.constant import WINDOW_HEIGHT, WINDOW_WIDTH


class MakeEnemy:
    
    ENEMY_BOX_SIZE = 20

    def __init__(self, dictionary, img=None) -> None:
        self._dict = dictionary
        self._img  = img
    
    def create_enemy_data(self, count):
        for i in range(count):
            key = f"enemy_{i+1}"
            rand_y = randint(1, WINDOW_HEIGHT-100)
            rand_x = randint(1, WINDOW_WIDTH-100)

            vol_x = randint(1,10)
            vol_y = randint(1,10)

            self._dict[key] = {
                "position": [rand_x, rand_y, rand_x + self.ENEMY_BOX_SIZE, rand_y + self.ENEMY_BOX_SIZE],
                "volocity": [vol_x, vol_y],
                "img": self._img
            }