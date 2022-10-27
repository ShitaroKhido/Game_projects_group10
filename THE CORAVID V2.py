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

=======
>>>>>>> c6565f8a6e7b4d37632f71342f6de8665f055139


def start():
    start_frame.pack(expand=True, fill=BOTH)
    


def setting(event):
    setting_frame.pack(expand=True, fill=BOTH)
    


def level1(event):
    level1_frame.pack(expand=True, fill=BOTH)



def level2(event):
    level2_frame.pack(expand=True, fill=BOTH)
    


def level3(event):
    level3_frame.pack(expand=True, fill=BOTH)
    

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
    # canvas.tag_bind("level_1", "<Button-1>", shoot)

    # canvas.tag_bind("button_start", "<Button-1>", start)
    # canvas.tag_bind("button_setting", "<Button-1>", setting)
    # canvas.tag_bind("button_exit", "<Button-1>", quit)
    # canvas.tag_bind("back_in_start", "<Button-1>", back_to_home)
    # canvas.tag_bind("back_in_game", "<Button-1>", back_to_start)
    # canvas.tag_bind("button_level1", "<Button-1>", level1)
    # canvas.tag_bind("button_level2", "<Button-1>", level2)
    # canvas.tag_bind("button_level3", "<Button-1>", level3)

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


home_canvas.create_rectangle(100,100,150,150, fill="black")





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
