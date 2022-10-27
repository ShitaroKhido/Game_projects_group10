from library.constant import *
from library.enemy import *
from tkinter import Button, Frame, Tk, Canvas, PhotoImage, Toplevel, mainloop, BOTH
from winsound import *


player_position = [200, 200, 240, 240]
bullet_count = []

#########################
#>>>>>> FUNCTIONS <<<<<<#
#########################
# .pack(expand=True, fill=BOTH)

def home():
    home_frame.pack(expand=True, fill=BOTH)
    start_btn.place(x=800, y=400)
    setting_btn.place(x=800, y=450)
    exit_btn.place(x=800, y=500)

def start():
    home_frame.destroy()
    start_frame.pack(expand=True, fill=BOTH)
    back_btn.place(x=20, y=20)
    level1_btn.place(x=140, y=150)
    level2_btn.place(x=390, y=150)
    level3_btn.place(x=640, y=150)

def setting():
    setting_frame.pack(expand=True, fill=BOTH)



#>>>>>> CHARACTER MOVEMENTS <<<<<<#

#>>>>>> SOUND <<<<<<#

#########################
#>>>>>> MAIN CODE <<<<<<#
#########################


# >>>>>> MAIN WINDOWS
root = Tk()
root.title(GAME_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(0, 0)


#>>>>>> Frame <<<<<<#
home_frame = Frame(root)
start_frame = Frame(root)
setting_frame = Frame(root)

#>>>>>> CANVAS <<<<<<#
home_canvas = Canvas(home_frame)
start_canvas = Canvas(start_frame)
setting_canvas = Canvas(setting_frame)


#>>>>>> PLAYER PROPERTIES <<<<<<#
player_crosshair_img = PhotoImage(file=CROSSHAIR)
enemy_img = PhotoImage(file=ENEMY_IMG_LOCATION)
player_img = PhotoImage(file=CHARACTER_IMG_LOCATION)
bullet_img = PhotoImage(file=BULLET_IMG_LOCATION)
player = None
# player_crosshair = canvas.create_rectangle(player_position)

#>>>>>> BACKGROUND <<<<<<#
background_home_img = PhotoImage(file=HOME_BACKGROUND_IMAGE_LOCATION)
background_black_img = PhotoImage(file=BLACK_IMG_LOCATION)
background_level1_img = PhotoImage(file=BACKGROUND_LEVEL1_LOCATION)
background_level2_img = PhotoImage(file=BACKGROUND_LEVEL2_LOCATION)
background_level3_img = PhotoImage(file=BACKGROUND_LEVEL3_LOCATION)
background_start_img = PhotoImage(file=BACKGROUND_START_LOCATION)
background_setting_img = PhotoImage(file=SETTING_IMAGE_LOCATION)


#>>>>>> BUTTON IMG<<<<<<#
button_start_img = PhotoImage(file=BUTTON_START_IMG_LOCATION)
button_setting_img = PhotoImage(file=BUTTON_SETTING_IMG_LOCATION)
button_exit_img = PhotoImage(file=BUTTON_EXIT_IMG_LOCATION)
button_back_img = PhotoImage(file=BUTTON_BACK_IMG_LOCATION)
button_level1_img = PhotoImage(file=BUTTON_LEVEL1_IMG_LOCATION)
button_level2_img = PhotoImage(file=BUTTON_LEVEL2_IMG_LOCATION)
button_level3_img = PhotoImage(file=BUTTON_LEVEL3_IMG_LOCATION)
button_on_img = PhotoImage(file=BUTTON_ON_IMG_LOCATION)
button_off_img = PhotoImage(file=BUTTON_OFF_IMG_LOCATION)


#>>>>>> BUTTON <<<<<<#

start_btn = Button(home_frame, image=button_start_img, command=start)
setting_btn = Button(home_frame, image=button_setting_img)
exit_btn = Button(home_frame, image=button_exit_img, command=quit)

back_btn = Button(start_frame, image=button_back_img)

level1_btn = Button(start_frame, image=button_level1_img)
level2_btn = Button(start_frame, image=button_level2_img)
level3_btn = Button(start_frame, image=button_level3_img)


home()




#>>>>>> HOME <<<<<<#
root.mainloop()
