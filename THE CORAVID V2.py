import winsound
from library.constant import *
from library.sprite import *
from tkinter import Button, Frame, Tk, Canvas, PhotoImage, Toplevel, mainloop, BOTH
from winsound import *


player_position = [200, 200, 240, 240]
bullet_count = []
enemy_data_dictionary = {}
player_health = 100
health_pos = [60, 60]
enemy_count = 20
enemy_size = 20

player_inventory = {}

items_data_dictionary = {}
item_img_list = []

#########################
#>>>>>> FUNCTIONS <<<<<<#
#########################


#>>>>>> CHARACTER MOVEMENTS <<<<<<#

def movement(x=0, y=0):
    canvas.move(player, x, y)


def move_right(event):
    movement(x=40)


def move_left(event):
    movement(x=-40)


def move_down(event):
    movement(y=40)


def move_up(event):
    movement(y=-40)


#>>>>>> PLAYERS CROSSHAIR AND AIMMING<<<<<<#

def crosshair(event):
    canvas.moveto(player_crosshair, event.x-AIM_ADJUSTMENT, event.y-AIM_ADJUSTMENT)


def shoot(event):
    global enemy_id
    hit = False
    target = (canvas.find_overlapping(event.x, event.y, event.x-AIM_ADJUSTMENT, event.y-AIM_ADJUSTMENT))
    for i in enemy_lists:
        if target[1] == enemy_lists[i]:
            enemy_id = i
            hit = True
            print(target)
    if hit:
        enemy_lists.pop(enemy_id)
        enemy_data_dictionary.pop(enemy_id)
        canvas.create_image(event.x,event.y,image=blood_img)
    if len(enemy_lists) <= 0:
        canvas.delete("all")
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-40,
                                       text="YOU SURVIVED", font=("impact", 100),
                                       fill="green"
                                       )
        winsound.PlaySound(WIN_SOUND, winsound.SND_FILENAME |
                       winsound.SND_ASYNC)


#>>>>>> ENEMY MOVEMENTS <<<<<<#

def build_enemy(enemy_dict_data):
    enemy_dict = {}
    for key in enemy_dict_data:
        enemy_dict[key] = canvas.create_image(
            enemy_dict_data[key]["position"], image=enemy_dict_data[key]["img_location"]
        )
    return enemy_dict


def enemy_move(lists):
    global player_health, health
    for key in enemy_data_dictionary:
        if canvas.coords(lists[key])[0] >= WINDOW_WIDTH:
            enemy_data_dictionary[key]["volocity"][0] = - \
                enemy_data_dictionary[key]["volocity"][0]

        elif canvas.coords(lists[key])[1] >= WINDOW_HEIGHT:
            enemy_data_dictionary[key]["volocity"][1] = - \
                enemy_data_dictionary[key]["volocity"][1]

        elif canvas.coords(lists[key])[0] <= 0:
            enemy_data_dictionary[key]["volocity"][0] = - \
                1*enemy_data_dictionary[key]["volocity"][0]

        elif canvas.coords(lists[key])[1] <= 0:
            enemy_data_dictionary[key]["volocity"][1] = - \
                1*enemy_data_dictionary[key]["volocity"][1]

        pos = canvas.coords(lists[key])
        over = canvas.find_overlapping(
            pos[0]-enemy_size, pos[1]-enemy_size, pos[0]+enemy_size, pos[1]+enemy_size)

        if len(over) > 2:
            if over[2] == player:
                player_health -= 4
                if health != None:
                    canvas.delete(health)
                if player_health <= 0:
                    canvas.delete(player)
                    canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-40,
                                       text="YOU DIED", font=("impact", 150),
                                       fill="red"
                                       )
                health = canvas.create_rectangle(
                    0, 0, player_health, 20, fill="red")
        canvas.move(lists[key],
                    enemy_data_dictionary[key]["volocity"][0], enemy_data_dictionary[key]["volocity"][1])
    canvas.after(40, lambda: enemy_move(lists))


#>>>>>> PLAYERS ITEMS <<<<<<#

def build_item(item_list_data):
    item_list = {}
    for key in item_list_data:
        item_list[key] = canvas.create_image(item_list_data[key]["position"], image=item_list_data[key]["img_location"])
    return item_list    
    


#>>>>>> GAME SPRITE DEPLOYMENTS <<<<<<#

def deploy_sprite(enemy_data: list, enemy_count:int):
    global player, health, player_crosshair, enemy_lists, player_laser
    
    enemy = MakeEnemy(enemy_data, enemy_img)
    enemy.create_enemy_data(enemy_count)
    enemy_lists = build_enemy(enemy_data)
    enemy_move(enemy_lists)

    health = canvas.create_rectangle(0, 0, player_health, 20, fill="red")
    player_crosshair = canvas.create_image(0, 0, image=player_crosshair_img)
    player = canvas.create_image(
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=player_img
    )
    player_laser = canvas.create_line(canvas.coords(player)[0], canvas.coords(player)[0],canvas.coords(player)[0], canvas.coords(player)[0])


#>>>>>> GUI CALL FUNCTION <<<<<<#

def home():
    winsound.PlaySound(MUSIC_HOME, winsound.SND_FILENAME |
                       winsound.SND_ASYNC)
    start_frame.pack_forget()
    home_frame.pack(expand=True, fill=BOTH)
    home_canvas.pack(expand=True, fill=BOTH)
    home_canvas.create_image(500, 300, image=background_home_img)
    home_canvas.create_image(890, 500, image=background_black_img)
    start_btn.place(x=810, y=400)
    setting_btn.place(x=810, y=465)
    exit_btn.place(x=810, y=530)


def start():
    winsound.PlaySound(MUSIC_CHOICE, winsound.SND_FILENAME |
                       winsound.SND_ASYNC)
    canvas.delete('all')
    canvas.pack_forget()
    home_frame.pack_forget()
    start_frame.pack(expand=True, fill=BOTH)
    start_canvas.pack(expand=True, fill=BOTH)
    start_canvas.create_image(500, 300, image=background_start_img)
    back_btn.place(x=20, y=20)
    level1_btn.place(x=140, y=200)
    level2_btn.place(x=390, y=200)
    level3_btn.place(x=640, y=200)


def setting():
    home_frame.pack_forget()
    setting_frame.pack(expand=True, fill=BOTH)
    setting_canvas.pack(expand=True, fill=BOTH)
    setting_canvas.create_image(500, 300, image=background_start_img)
    setting_canvas.create_image(500, 300, image=background_setting_img)
    back_btn.place(x=20, y=30)


#>>>>>> GUI CALL FUNCTIONS LEVELS <<<<<<#

def level_1():
    in_game_music()
    start_frame.pack_forget()
    canvas.pack(expand=True, fill=BOTH)
    canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT /
                        2, image=background_level1_img)
    deploy_sprite(enemy_data_dictionary, 1)
    print(player)



def level_2():
    in_game_music()
    start_frame.pack_forget()
    canvas.pack(expand=True, fill=BOTH)
    canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT /
                        2, image=background_level2_img)
    deploy_sprite(enemy_data_dictionary, 20)
    print(player)


def level_3():
    in_game_music()
    start_frame.pack_forget()
    canvas.pack(expand=True, fill=BOTH)
    canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT /
                        2, image=background_level3_img)
    deploy_sprite(enemy_data_dictionary, 30)
    print(player)

def in_game_music():
    winsound.PlaySound(MUSIC_IN_GAME, winsound.SND_FILENAME |
                       winsound.SND_ASYNC)
#########################
#>>>>>> MAIN CODE <<<<<<#
#########################
# >>>>>> MAIN WINDOWS

root = Tk()
root.title(GAME_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(0, 0)


#>>>>>> ROOT CANVAS <<<<<<#

canvas = Canvas(root)
# canvas.pack(expand=True, fill=BOTH)


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

#>>>>>>>>> ITEM IMG <<<<<<<<#
green_virus_img=PhotoImage(file=GREEN_VIRUS_LOCATION)
heart_img=PhotoImage(file=HEART_LOCATION)
red_virus_img=PhotoImage(file=RED_VIRUS_LOCATIO)
vacinne_img=PhotoImage(file=VACINNE_LOCATION)
virus_2_img=PhotoImage(file=VIRUS_2_LOCATION)
virus_3_img=PhotoImage(file=VIRUS_3_LOCATION)
blood_img=PhotoImage(file=BLOOD_LOCATION)

#>>>>>> HOME FRAME BUTTON <<<<<<#

start_btn = Button(home_frame, image=button_start_img, command=start)
setting_btn = Button(home_frame, image=button_setting_img, command=setting)
exit_btn = Button(home_frame, image=button_exit_img, command=quit)


#>>>>>> START FRAME BUTTON <<<<<<#
back_btn = Button(start_frame, image=button_back_img, command=home)
level1_btn = Button(start_frame, image=button_level1_img, command=level_1)
level2_btn = Button(start_frame, image=button_level2_img, command=level_2)
level3_btn = Button(start_frame, image=button_level3_img, command=level_3)


############################################
#>>>>>> FUNCTIONS DEPLOYMENT HERE!!! <<<<<<#
############################################

home()


#>>>>>> KEY BINDING <<<<<<#

root.bind("<w>", move_up)
root.bind("<a>", move_left)
root.bind("<s>", move_down)
root.bind("<d>", move_right)

root.bind("<Motion>", crosshair)
root.bind("<Button-1>", shoot)

root.mainloop()
