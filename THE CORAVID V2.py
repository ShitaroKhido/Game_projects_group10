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
    button_start.place(x=816, y=400 )
    button_setting.place (x=816, y=470)
    button_exit.place (x=816, y=540)


def start():
    home_frame.forget()
    start_frame.pack(expand=True, fill=BOTH)
    start_canvas.pack(expand=True, fill=BOTH)
    start_canvas.create_image(500, 300, image=background_start_img)
    start_canvas.create_image(
        70, 40, image=button_back_img, tags='back_in_start')
    button_back_home.place(x=10,y=10)
    button_level1 .place( x = 100, y = 250)
    button_level2 .place ( x = 390, y = 250)
    button_level3 .place( x = 680, y = 250)


def setting():
    home_frame.forget()
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
<<<<<<< HEAD
    global level1_top
    level1_top = Toplevel(root)
=======
    start_frame.forget()
    global level1_canvas
    level1_frame.pack(expand=True, fill=BOTH)
>>>>>>> e0278bb99270a14da0aca9a210162756eda8ec5e
    level1_canvas.pack(expand=True, fill=BOTH)

    level1_canvas.create_image(500, 120, image=background_level1_img)
    level1_canvas.create_image(
        70, 560, image=button_back_img, tags='back_in_game')
    deploy_sprite(level1_top, level1_canvas, 20)


def level2(event):
    global level2_top
    level2_top = Toplevel(root)
def level2():
    start_frame.forget()
    level2_frame.pack(expand=True, fill=BOTH)
    level2_canvas.pack(expand=True, fill=BOTH)
    level2_canvas.create_image(500, 120, image=background_level2_img)
    level2_canvas.create_image(
        70, 560, image=button_back_img, tags='back_in_game')


def level3(event):
    global level3_top
    level3_top = Toplevel(root)
def level3():
    start_frame.forget()
    level3_frame.pack(expand=True, fill=BOTH)
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
button_start=Button(home_canvas,image=button_start_img,command=start)
button_setting=Button(home_canvas,image=button_setting_img,command=setting)
button_exit=Button(home_canvas,image=button_exit_img,command=root.destroy)
button_back_home=Button(start_canvas,image=button_back_img,command=back_to_home)

button_level1=Button(start_canvas,image=button_level1_img,command=level1)
button_level2=Button(start_canvas,image=button_level2_img,command=level2)
button_level3=Button(start_canvas,image=button_level3_img,command=level3)



level1()




#>>>>>> HOME <<<<<<#
root.mainloop()
