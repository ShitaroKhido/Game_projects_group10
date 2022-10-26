from tkinter import Button, Frame, PhotoImage, Tk, Canvas, mainloop, BOTH
from Game_projects_group10.mechanism import *

 

### CONSTANT
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

  
root = Tk()
root.title(GAME_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

main_canvas = Canvas(root)
main_canvas.pack(expand=True, fill=BOTH)
root.mainloop()
