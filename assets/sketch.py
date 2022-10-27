
#### UNUSED ####



# class Character:
    
#     def __init__(self, master_window, main_canvas, player_canvas):
#         self._master = master_window
#         self._canvas = main_canvas
#         self._player = player_canvas
#         #### PLAYER COORDINATION
#         self._coord = self._canvas.coords(self._player)
#         self._crosshair = None

#     def get_coord(self):
#         return self._coord

#     def aim(self, event):
#         self._canvas.moveto(self._crosshair, event.x-40, event.y-40)

#     def crosshair(self, crosshair_image):
#         self._crosshair = self._canvas.create_image(self._coord[0], self._coord[0], image=crosshair_image)


# class Movements(Character):
    
#     MOVES_VOLOCITY = 60
#     PLATFORM_SIZE = [1000, 600]

#     def __init__(self, master_window, main_canvas, player_canvas):
#         super().__init__(master_window, main_canvas, player_canvas)

#     def move_character(self, x=0, y=0):
#         self._canvas.move(self._player, x, y)

#     def move_right(self, event):
#         self.move_character(x = self.MOVES_VOLOCITY)
    
#     def move_left(self, event):
#         self.move_character( x = -(self.MOVES_VOLOCITY))
    
#     def move_up(self, event):
#         self.move_character( y = -(self.MOVES_VOLOCITY))

#     def move_down(self, event):
#         self.move_character( y = self.MOVES_VOLOCITY)

