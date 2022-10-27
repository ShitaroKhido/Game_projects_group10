from library.constant import *
from library.enemy import *
from tkinter import Tk, Canvas, PhotoImage, mainloop, BOTH
from winsound import *


player_position = [200, 200, 240, 240]


#########################
#>>>>>> FUNCTIONS <<<<<<#
#########################

#>>>>>> CHARACTER MOVEMENTS <<<<<<#
def movement(canvas_id, x, y):
    canvas.move(canvas_id, x, y)


def move_left(event):
    movement(canvas_id=player, x=-40)


def move_right(event):
    movement(canvas_id=player, x=40)


def move_up(event):
    movement(canvas_id=player, y=-40)


def move_down(event):
    movement(canvas_id=player, y=40)


def deploy_sprite(number_of_enemy: int):
    player_box = canvas.create_oval(player_position, fill="black")
    player = canvas.create_image(player_position[0])
    enemy = Enemy()
    enemy.number_of_enemy(number_of_enemy)


def home():
    canvas.delete('all')
    canvas.create_image(500, 300, image=background_home_img)
    canvas.create_image(890, 500, image=background_black_img)
    button_start = canvas.create_image(
        890, 430, image=button_start_img, tags='button_start')
    button_setting = canvas.create_image(
        890, 495, image=button_setting_img, tags='button_setting')
    button_exit = canvas.create_image(
        890, 560, image=button_exit_img, tags='button_exit')
    pass


def start(event):
    PlaySound(MUSIC_CHOICE, SND_FILENAME | SND_ASYNC)
    canvas.create_image(500, 300, image=background_start_img)
    canvas.create_image(
        70, 40, image=button_back_img, tags='back_in_start')
    button_level1 = canvas.create_image(
        200, 300, image=button_level1_img, tags='button_level1')
    button_level2 = canvas.create_image(
        500, 300, image=button_level2_img, tags='button_level2')
    button_level3 = canvas.create_image(
        800, 300, image=button_level3_img, tags='button_level3')


def setting(event):
    canvas.delete('all')
    canvas.create_image(500, 300, image=background_start_img)
    canvas.create_image(500, 300, image=background_setting_img)
    canvas.create_image(
        70, 40, image=button_back_img, tags='back_in_start')

    sound_on = canvas.create_image(
        600, 155, image=button_on_img, tags='button_on')
    sound_off = canvas.create_image(
        700, 155, image=button_off_img, tags='button_off')
    music_on = canvas.create_image(
        600, 250, image=button_on_img, tags='button_on')
    music_off = canvas.create_image(
        700, 250, image=button_off_img, tags='button_off')


def level1(event):
    canvas.delete('all')
    canvas.create_image(500, 120, image=background_level1_img)
    deploy_sprite(10)
    Inlevel()


def level2(event):
    canvas.delete('all')
    canvas.create_image(500, 120, image=background_level2_img)
    Inlevel()


def level3(event):
    canvas.delete('all')
    canvas.create_image(500, 300, image=background_level3_img)
    Inlevel()


def Inlevel():
    PlaySound(MUSIC_IN_GAME, SND_FILENAME | SND_ASYNC)
    canvas.create_image(
        70, 560, image=button_back_img, tags='back_in_game')


def back_to_home(event):
    home()


def back_to_start(event):
    start(event)


def key_bind():
    root.bind("<w>", move_up)
    root.bind("<a>", move_left)
    root.bind("<s>", move_down)
    root.bind("<d>", move_right)

    canvas.tag_bind("button_start", "<Button-1>", start)
    canvas.tag_bind("button_setting", "<Button-1>", setting)
    canvas.tag_bind("button_exit", "<Button-1>", quit)
    canvas.tag_bind("back_in_start", "<Button-1>", back_to_home)
    canvas.tag_bind("back_in_game", "<Button-1>", back_to_start)
    canvas.tag_bind("button_level1", "<Button-1>", level1)
    canvas.tag_bind("button_level2", "<Button-1>", level2)
    canvas.tag_bind("button_level3", "<Button-1>", level3)

#########################
#>>>>>> MAIN CODE <<<<<<#
#########################


# >>>>>> MAIN WINDOWS
root = Tk()
root.title(GAME_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(0, 0)


#>>>>>> MAIN CANVAS <<<<<<#
canvas = Canvas(root)
canvas.pack(expand=True, fill=BOTH)


#>>>>>> PLAYER PROPERTIES <<<<<<#
player_crosshair = PhotoImage(file=CROSSHAIR)
enemy_img = PhotoImage(file=ENEMY_IMG_LOCATION)
player_img = PhotoImage(file=CHARACTER_IMG_LOCATION)
bullet_img = PhotoImage(file=BULLET_IMG_LOCATION)
player = None

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


#>>>>>> HOME <<<<<<#
home()
key_bind()
root.mainloop()
