from tkinter import Button, Frame, PhotoImage, Tk, Canvas, mainloop, BOTH
from Mechanism import *

 
################
### CONSTANT ###
################

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_TITLE = "THE CORAVID"

GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = ""
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"
CROSSHAIR = "Game_projects_group10\\assets\image\crosshairs.png"
ENEMY_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"
#################
### MAIN CODE ###
#################

###### GUI WINDOWS INTERFACE ######
root = Tk()
root.title(GAME_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(0,0)

###### MAIN CANVAS ######
main_canvas = Canvas(root)
main_canvas.pack(expand=True, fill=BOTH)

###### PLAYER CANVAS ######
player_canvas = main_canvas.create_oval(100,100, 150,150)
player_crosshair = PhotoImage(file=CROSSHAIR)
###### PLAYER FUNTION ######
main_player = Movements(root, main_canvas, player_canvas)
main_player.crosshair(player_crosshair)


enemy_img = PhotoImage(file=ENEMY_IMG_LOCATION)
enemy = Enemy(root, main_canvas, enemy_img)
enemy.number_of_enemy(10)
enemy.enem_dictionary()
enemy.move_enemy()
root.bind("<Motion>", main_player.aim)


###### PLAYER KEY BIND ######
root.bind("<w>", main_player.move_up)
root.bind("<a>", main_player.move_left)
root.bind("<s>", main_player.move_down)
root.bind("<d>", main_player.move_right)

root.mainloop()
