from library.constant import *
from library.enemy import *
from tkinter import Button, Frame, Tk, Canvas, PhotoImage, Toplevel, mainloop, BOTH
from winsound import *


player_position = [200, 200, 240, 240]
bullet_count = []

#########################
#>>>>>> FUNCTIONS <<<<<<#
#########################

#>>>>>> CHARACTER MOVEMENTS <<<<<<#

# def shoot(event):
#     a = (canvas.coords(player_box)[2]+canvas.coords(player_box)[0])/2
#     b = (canvas.coords(player_box)[3]+canvas.coords(player_box)[1])/2

#     x = event.x - a
#     y = event.y - b

#     canvas.move(bullet,(x+2)-(x-2)/2, (y+2)-(y-2)/2 )
#     aft = canvas.after(100, lambda:shoot(event))


def deploy_sprite(frame, canvas, number_of_enemy: int):
    global player, player_box
    player_box = canvas.create_oval(player_position, fill="black")
    player = canvas.create_image(
        player_position[0], player_position[2], image=player_img)
    enemy = Enemy(frame, canvas, enemy_img)
    enemy.number_of_enemy(number_of_enemy)
    enemy.move_enemy()

    key_bind(frame)


def number_bullet(number: int, bullet_size=10):
    pass


#>>>>>> INTERFACE <<<<<<#
def home():
    home_frame.pack(expand=True, fill=BOTH)
    home_canvas.pack(expand=True, fill=BOTH)
    home_canvas.create_image(500, 300, image=background_home_img)
    home_canvas.create_image(890, 500, image=background_black_img)
    button_start = home_canvas.create_image(
        890, 430, image=button_start_img, tags='button_start')
    button_setting = home_canvas.create_image(
        890, 495, image=button_setting_img, tags='button_setting')
    button_exit = home_canvas.create_image(
        890, 560, image=button_exit_img, tags='button_exit')


def start(event):
    start_frame.pack(expand=True, fill=BOTH)
    start_canvas.pack(expand=True, fill=BOTH)

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
    setting_canvas.pack(expand=True, fill=BOTH)

    setting_canvas.create_image(500, 300, image=background_start_img)
    setting_canvas.create_image(500, 300, image=background_setting_img)
    setting_canvas.create_image(
        70, 40, image=button_back_img, tags='back_in_start')

    sound_on = setting_canvas.create_image(
        600, 155, image=button_on_img, tags='button_on')
    sound_off = setting_canvas.create_image(
        700, 155, image=button_off_img, tags='button_off')
    music_on = setting_canvas.create_image(
        600, 250, image=button_on_img, tags='button_on')
    music_off = setting_canvas.create_image(
        700, 250, image=button_off_img, tags='button_off')


def level1():
    global level1_top
    level1_top = Toplevel(root)
    level1_canvas.pack(expand=True, fill=BOTH)

    level1_canvas.create_image(500, 120, image=background_level1_img)
    level1_canvas.create_image(
        70, 560, image=button_back_img, tags='back_in_game')
    deploy_sprite(level1_top, level1_canvas, 20)


def level2():
    global level2_top
    level2_top = Toplevel(root)
    level2_canvas.pack(expand=True, fill=BOTH)
    level2_canvas.create_image(500, 120, image=background_level2_img)
    level2_canvas.create_image(
        70, 560, image=button_back_img, tags='back_in_game')


def level3():
    global level3_top
    level3_top = Toplevel(root)
    level3_canvas.pack(expand=True, fill=BOTH)
    level3_canvas.create_image(500, 300, image=background_level3_img)
    level3_canvas.create_image(
        70, 560, image=button_back_img, tags='back_in_game')
    

#>>>>>> SOUND <<<<<<#


def Inlevel():
    pass


def back_to_home(event):
    home()


def back_to_start(event):
    start(event)


def key_bind(master):
    # master.bind("<w>", move_up)
    # master.bind("<a>", move_left)
    # master.bind("<s>", move_down)
    # master.bind("<d>", move_right)
    # master.bind("<Motion>", crosshair)
    pass


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
level3_top = Toplevel(root)

#>>>>>> CANVAS <<<<<<#
home_canvas = Canvas(home_frame)
start_canvas = Canvas(start_frame)
setting_canvas = Canvas(setting_frame)
level1_canvas = Canvas(level1_top)
level2_canvas = Canvas(level2_top)
level3_canvas = Canvas(level3_top)

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



level1()




#>>>>>> HOME <<<<<<#
root.mainloop()
