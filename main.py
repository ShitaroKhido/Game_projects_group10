from tkinter import PhotoImage, Tk, Canvas, mainloop, BOTH


### CONSTANT
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600


GAME_TITLE = "THE CORAVID"
GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"

BACKGROUND_LEVEL_ONE="Game_projects_group10\\assets\image\LEVEL1.png"
BACKGROUND_LEVEL_TWO="Game_projects_group10\\assets\image\LEVEL2.png"
BACKGROUND_LEVEL_THREE="Game_projects_group10\\assets\image\LEVEL3.png"
#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")


    mainloop()
