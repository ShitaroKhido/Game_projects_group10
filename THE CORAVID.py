from tkinter import Button, Frame, PhotoImage, Tk, Canvas, mainloop, BOTH
from mechanism import *

 
################
### CONSTANT ###
################

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_TITLE = "THE CORAVID"

GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"
CROSSHAIR = "Game_projects_group10\\assets\image\crosshairs.png"

#################
### MAIN CODE ###
#################

###### GUI WINDOWS INTERFACE ######
root = Tk()
root.title(GAME_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

###### MAIN CANVAS ######
main_canvas = Canvas(root)
main_canvas.pack(expand=True, fill=BOTH)

###### PLAYER CANVAS ######
player_canvas = main_canvas.create_oval(100,100, 150,150)

###### PLAYER FUNTION ######
main_player = Character(main_canvas, player_canvas)

###### PLAYER KEY BIND ######
root.bind("<w>", main_player.move_up)
root.bind("<a>", main_player.move_left)
root.bind("<s>", main_player.move_down)
root.bind("<d>", main_player.move_right)

root.mainloop()
