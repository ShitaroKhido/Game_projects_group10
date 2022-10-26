from tkinter import Frame, PhotoImage, Tk, Canvas, mainloop, BOTH


### CONSTANT
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_TITLE = "THE CORAVID"

GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"

#################
### MAIN CODE ###
#################

if __name__ == "__main__":
    
    root = Tk()
    root.title(GAME_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    ### MAIN GAME FRAME
    frame = Frame(root)
    frame.pack(expand=True, fill=BOTH)
    ### MAIN CANVAS
    canvas = Canvas(frame)
    canvas.pack(expand=True, fill=BOTH)
    ### PLAYER IMAGES
    player_img = PhotoImage(file=CHARACTER_IMG_LOCATION)

    main_player = Player(frame, canvas, [100,100], player_img)


    mainloop()
