from library.constant import *
from library.enemy import *
from tkinter import Frame, Tk, Canvas, PhotoImage, mainloop, BOTH
from winsound import *


player_position = [200, 200, 240, 240]
bullet_count = []

#########################
#>>>>>> FUNCTIONS <<<<<<#
#########################

#>>>>>> CHARACTER MOVEMENTS <<<<<<#
def movement(x=0, y=0):
    # canvas.move(player, x, y)
    # canvas.move(player_box, x, y)
    pass


def move_left(event):
    movement(x=-40)


def move_right(event):
    movement(x=40)


def move_up(event):
    movement(y=-40)


def move_down(event):
    movement(y=40)


def crosshair(event):
    pass

# def shoot(event):
#     a = (canvas.coords(player_box)[2]+canvas.coords(player_box)[0])/2
#     b = (canvas.coords(player_box)[3]+canvas.coords(player_box)[1])/2
    
#     x = event.x - a
#     y = event.y - b

#     canvas.move(bullet,(x+2)-(x-2)/2, (y+2)-(y-2)/2 )
#     aft = canvas.after(100, lambda:shoot(event))



def deploy_sprite(number_of_enemy: int):
    pass



def number_bullet(number: int, bullet_size=10):
    pass
        





#>>>>>> INTERFACE <<<<<<#
def home():
    home_frame.pack(expand=True, fill=BOTH)
<<<<<<< HEAD
    home_frame.create_image(500, 300, image=background_home_img)
    home_frame.create_image(890, 500, image=background_black_img)
    button_start = home_frame.create_image(
        890, 430, image=button_start_img, tags='button_start')
    button_setting = home_frame.create_image(
        890, 495, image=button_setting_img, tags='button_setting')
    button_exit = home_frame.create_image(
        890, 560, image=button_exit_img, tags='button_exit')
=======

>>>>>>> e63fb4e70c88c5c2d7cb3e9e62eed9a89bfca770

def start():
    start_frame.pack(expand=True, fill=BOTH)
    winsound.PlaySound(MUSIC_CHOICE, winsound.SND_FILENAME |
                       winsound.SND_ASYNC)
    start_frame.create_image(500, 300, image=background_start_img)
    start_frame.create_image(
        70, 40, image=button_back_img, tags='back_in_start')
    button_level1 = start_frame.create_image(
        200, 300, image=button_level1_img, tags='button_level1')
    button_level2 = start_frame.create_image(
        500, 300, image=button_level2_img, tags='button_level2')
    button_level3 = start_frame.create_image(
        800, 300, image=button_level3_img, tags='button_level3')


def setting(event):
    setting_frame.pack(expand=True, fill=BOTH)
    


def level1(event):
    level1_frame.pack(expand=True, fill=BOTH)
    level1_canvas.create_image(500, 120, image=background_level1_img)
    


def level2(event):
    level2_frame.pack(expand=True, fill=BOTH)
    level2_canvas.create_image(500, 120, image=background_level2_img)
    


def level3(event):
    level3_frame.pack(expand=True, fill=BOTH)
    level3_canvas.create_image(500, 300, image=background_level3_img)
    

#>>>>>> SOUND <<<<<<#


def Inlevel():
    pass


def back_to_home(event):
    home()


def back_to_start(event):
    start(event)


def key_bind():
    root.bind("<w>", move_up)
    root.bind("<a>", move_left)
    root.bind("<s>", move_down)
    root.bind("<d>", move_right)
    root.bind("<Motion>", crosshair)


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
level1_frame = Frame(root)
level2_frame = Frame(root)
level3_frame = Frame(root)


#>>>>>> CANVAS <<<<<<#
home_canvas = Canvas(home_frame)
<<<<<<< HEAD
start_frame = Canvas(start_frame)
setting_frame = Canvas(setting_frame)

=======
level1_canvas = Canvas(level1_frame)
level2_canvas = Canvas(level2_frame)
level3_canvas = Canvas(level3_frame)
>>>>>>> e63fb4e70c88c5c2d7cb3e9e62eed9a89bfca770





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


#>>>>>> BUTTON <<<<<<#
button_start_img = PhotoImage(file=BUTTON_START_IMG_LOCATION)
button_setting_img = PhotoImage(file=BUTTON_SETTING_IMG_LOCATION)
button_exit_img = PhotoImage(file=BUTTON_EXIT_IMG_LOCATION)
button_back_img = PhotoImage(file=BUTTON_BACK_IMG_LOCATION)
button_level1_img = PhotoImage(file=BUTTON_LEVEL1_IMG_LOCATION)
button_level2_img = PhotoImage(file=BUTTON_LEVEL2_IMG_LOCATION)
button_level3_img = PhotoImage(file=BUTTON_LEVEL3_IMG_LOCATION)
button_on_img = PhotoImage(file=BUTTON_ON_IMG_LOCATION)
button_off_img = PhotoImage(file=BUTTON_OFF_IMG_LOCATION)

home()
#>>>>>> HOME <<<<<<#
root.mainloop()
