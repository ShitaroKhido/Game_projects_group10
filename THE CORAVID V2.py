from library.constant import *
from library.sprite import *
from tkinter import Button, Frame, Tk, Canvas, PhotoImage, Toplevel, mainloop, BOTH
from winsound import *

player_inventory = {}
player_health = 200

bullet_count = []
health_pos = [60, 60]

enemy_data_dictionary = {}
enemy_size = 20

level_count = 0

#########################
#>>>>>> FUNCTIONS <<<<<<#
#########################

###################################
#>>>>>> CHARACTER MOVEMENTS <<<<<<#
###################################


def movement(x=0, y=0):
    is_not_wall = True
    if canvas.coords(player)[0] + x >= WINDOW_WIDTH or\
            canvas.coords(player)[1] + y >= WINDOW_HEIGHT or\
            canvas.coords(player)[0] + x <= 0 or\
            canvas.coords(player)[1] + y <= 0:
        is_not_wall = False
        return_value = None
    elif is_not_wall:
        return_value = canvas.move(player, x, y)
    return return_value


def move_right(event):
    movement(x=40)


def move_left(event):
    movement(x=-40)


def move_down(event):
    movement(y=40)


def move_up(event):
    movement(y=-40)


############################################
#>>>>>> PLAYERS CROSSHAIR AND AIMMING<<<<<<#
############################################

def crosshair(event):
    canvas.moveto(player_crosshair, event.x -
                  AIM_ADJUSTMENT, event.y-AIM_ADJUSTMENT)


def shoot(event):
    global enemy_id, up_count, enemy_data_dictionary, enemy_lists, shot_sound, level_count
    hit = False
    target = (canvas.find_overlapping(event.x, event.y,
              event.x-AIM_ADJUSTMENT, event.y-AIM_ADJUSTMENT))
    shot_sound = PlaySound(LASER_SHOT, SND_FILENAME |
                           SND_ASYNC)

    # >>> CHECK ENEMY ID WHEN
    for i in enemy_lists:
        if target[1] == enemy_lists[i]:
            enemy_id = i
            hit = True
            print(target)

    # >>> IF HIT THE ENEMY RUN THIS BLOCK
    if hit:
        canvas.delete(enemy_lists[enemy_id])
        enemy_lists.pop(enemy_id)
        enemy_data_dictionary.pop(enemy_id)
        blood_splash = canvas.create_image(event.x, event.y, image=blood_img)
        canvas.after(100, lambda: canvas.delete(blood_splash))

    # >>> CHECK IF NO ENEMY
    if len(enemy_lists) <= 0:
        canvas.delete("all")
        level_count += 1
        if level_count == 1:
            win_screen("Moving to level 2", "black", level_2)
        elif level_count == 2:
            win_screen("Moving to level 2", "black", level_3)

        elif level_count == 3:
            win_screen("You have finish the game", "black", start)
        enemy_data_dictionary.clear()
        enemy_lists.clear()

    print(len(enemy_lists))


def win_screen(text: str, color: str, toWhere):
    canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-40,
                       text=text, font=("impact", 80),
                       fill=color
                       )
    root.after(1000, toWhere)


###############################
#>>>>>> ENEMY MOVEMENTS <<<<<<#
###############################

def build_enemy(enemy_dict_data):
    enemy_dict = {}
    for key in enemy_dict_data:
        enemy_dict[key] = canvas.create_image(
            enemy_dict_data[key]["position"], image=enemy_dict_data[key]["img_location"]
        )
    return enemy_dict


def enemy_move(lists):
    global player_health, health, restart_btn_level1
    intersect_adjustment = 40
    for key in enemy_data_dictionary:
        if canvas.coords(lists[key])[0] >= WINDOW_WIDTH-intersect_adjustment:
            enemy_data_dictionary[key]["volocity"][0] = - \
                enemy_data_dictionary[key]["volocity"][0]

        elif canvas.coords(lists[key])[1] >= WINDOW_HEIGHT-intersect_adjustment:
            enemy_data_dictionary[key]["volocity"][1] = - \
                enemy_data_dictionary[key]["volocity"][1]

        elif canvas.coords(lists[key])[0] <= intersect_adjustment:
            enemy_data_dictionary[key]["volocity"][0] = - \
                1*enemy_data_dictionary[key]["volocity"][0]

        elif canvas.coords(lists[key])[1] <= intersect_adjustment:
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
                                       fill="red")
                    PlaySound(GAME_OVER_SOUND, SND_FILENAME |
                              SND_ASYNC)
                    if level_count == 0:
                        restart_btn_level1.place(x=400, y=400)
                    elif level_count == 1:
                        restart_btn_level2.place(x=400, y=400)
                    elif level_count == 2:
                        restart_btn_level3.place(x=400, y=400)
                    player_health = 200
                health = canvas.create_rectangle(
                    0, 0, player_health, 20, fill="red")
        canvas.move(lists[key],
                    enemy_data_dictionary[key]["volocity"][0], enemy_data_dictionary[key]["volocity"][1])
    canvas.after(40, lambda: enemy_move(lists))


#######################################
#>>>>>> GAME SPRITE DEPLOYMENTS <<<<<<#
#######################################

def deploy_sprite(enemy_data: list, enemy_count: int, enemy_img):
    global player, health, player_crosshair, enemy_lists, player_laser

    enemy = MakeEnemy(enemy_data, enemy_img)
    enemy.create_enemy_data(enemy_count)
    enemy_lists = build_enemy(enemy_data)
    enemy_move(enemy_lists)

    health = canvas.create_rectangle(0, 0, player_health, 20, fill="red")

    root.bind("<Motion>", crosshair)
    root.bind("<Button-1>", shoot)

    player = canvas.create_image(
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=player_img)
    player_laser = canvas.create_line(canvas.coords(player)[0], canvas.coords(
        player)[0], canvas.coords(player)[0], canvas.coords(player)[0])
    player_crosshair = canvas.create_image(0, 0, image=player_crosshair_img)


#################################
#>>>>>> GUI CALL FUNCTION <<<<<<#
#################################

def upgrade(event):
    setting_window_ingame = Toplevel(root)
    setting_window_ingame.geometry("250x200")
    setting_window_ingame.resizable(0, 0)

    add_health = Button(setting_window_ingame, text="ADD HEALTH", pady=20)
    add_health.pack(expand=True, fill="x")

    reset_game = Button(setting_window_ingame, text="Reset game", pady=20)
    reset_game.pack(expand=True, fill="x")

    exit_game = Button(setting_window_ingame, text="Exit", pady=20)
    exit_game.pack(expand=True, fill="x")


def home():
    PlaySound(MUSIC_HOME, SND_FILENAME |
              SND_ASYNC)
    start_frame.pack_forget()
    home_frame.pack(expand=True, fill=BOTH)
    home_canvas.pack(expand=True, fill=BOTH)
    home_canvas.create_image(500, 300, image=background_home_img)
    start_btn.place(x=800, y=340)
    setting_btn.place(x=800, y=415)
    exit_btn.place(x=800, y=490)


def start():
    canvas.delete('all')
    canvas.pack_forget()
    home_frame.pack_forget()
    start_frame.pack(expand=True, fill=BOTH)
    start_canvas.pack(expand=True, fill=BOTH)
    start_canvas.create_image(500, 300, image=background_start_img)
    back_btn.place(x=50, y=20)
    level1_btn.place(x=50, y=200)
    level2_btn.place(x=370, y=200)
    level3_btn.place(x=690, y=200)


def setting():
    home_frame.pack_forget()
    setting_frame.pack(expand=True, fill=BOTH)
    setting_canvas.pack(expand=True, fill=BOTH)
    setting_canvas.create_image(500, 300, image=background_start_img)
    setting_canvas.create_image(500, 300, image=background_setting_img)
    back_btn.place(x=20, y=30)


#########################################
#>>>>>> GUI CALL FUNCTIONS LEVELS <<<<<<#
#########################################
def restart_from_level_1():
    canvas.delete('all')
    level_1()


def restart_from_level_2():
    canvas.delete('all')
    level_2()


def restart_from_level_3():
    canvas.delete('all')
    level_3()


def level_1():
    global main_window_sound, restart_btn_level1
    canvas.delete('all')
    restart_btn_level1.place_forget()
    main_window_sound = PlaySound(MUSIC_CHOICE, SND_FILENAME |
                                  SND_ASYNC)
    start_frame.pack_forget()
    canvas.pack(expand=True, fill=BOTH)
    canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT /
                        2, image=background_level1_img)
    deploy_sprite(enemy_data_dictionary,
                  1, enemy_img_lv1)


def level_2():
    global restart_btn_level2
    canvas.delete('all')

    restart_btn_level2.place_forget()
    start_frame.pack_forget()
    canvas.pack(expand=True, fill=BOTH)
    canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT /
                        2, image=background_level2_img)
    deploy_sprite(enemy_data_dictionary,
                  NUMBER_OF_ENEMY_LEVEL_2, enemy_img_lv2)


def level_3():
    global restart_btn_level3
    canvas.delete('all')
    start_frame.pack_forget()
    restart_btn_level3.place_forget()
    canvas.pack(expand=True, fill=BOTH)
    canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT /
                        2, image=background_level3_img)
    deploy_sprite(enemy_data_dictionary,
                  NUMBER_OF_ENEMY_LEVEL_3, enemy_img_lv3)


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


#>>>>>> PLAYER IMG <<<<<<#
player_crosshair_img = PhotoImage(file=CROSSHAIR)
player_img = PhotoImage(file=CHARACTER_IMG_LOCATION)
bullet_img = PhotoImage(file=BULLET_IMG_LOCATION)
player = None


#>>>>>> ENEMY IMG <<<<<<#
enemy_img_lv1 = PhotoImage(file=ENEMY_IMG_LOCATION)
enemy_img_lv2 = PhotoImage(file=ENEMY2_IMG_LOCATION)
enemy_img_lv3 = PhotoImage(file=ENEMY3_IMG_LOCATION)


#>>>>>> BACKGROUND <<<<<<#
background_home_img = PhotoImage(file=HOME_BACKGROUND_IMAGE_LOCATION)
background_black_img = PhotoImage(file=BLACK_IMG_LOCATION)
background_level1_img = PhotoImage(file=BACKGROUND_LEVEL1_LOCATION)
background_level2_img = PhotoImage(file=BACKGROUND_LEVEL2_LOCATION)
background_level3_img = PhotoImage(file=BACKGROUND_LEVEL3_LOCATION)
background_start_img = PhotoImage(file=BACKGROUND_START_LOCATION)
background_setting_img = PhotoImage(file=SETTING_IMAGE_LOCATION)


#>>>>>> BUTTON IMG <<<<<<#
button_start_img = PhotoImage(file=BUTTON_START_IMG_LOCATION)
button_setting_img = PhotoImage(file=BUTTON_SETTING_IMG_LOCATION)
button_exit_img = PhotoImage(file=BUTTON_EXIT_IMG_LOCATION)
button_back_img = PhotoImage(file=BUTTON_BACK_IMG_LOCATION)
button_level1_img = PhotoImage(file=BUTTON_LEVEL1_IMG_LOCATION)
button_level2_img = PhotoImage(file=BUTTON_LEVEL2_IMG_LOCATION)
button_level3_img = PhotoImage(file=BUTTON_LEVEL3_IMG_LOCATION)
button_on_img = PhotoImage(file=BUTTON_ON_IMG_LOCATION)
button_off_img = PhotoImage(file=BUTTON_OFF_IMG_LOCATION)
button_restart_img = PhotoImage(file=BUTTON_RESTART_IMG_LOCATION)


#>>>>>>>>> ITEM IMG <<<<<<<<#
green_virus_img = PhotoImage(file=GREEN_VIRUS_LOCATION)
heart_img = PhotoImage(file=HEART_LOCATION)
red_virus_img = PhotoImage(file=RED_VIRUS_LOCATION)
vacinne_img = PhotoImage(file=VACINNE_LOCATION)
blood_img = PhotoImage(file=BLOOD_LOCATION)
item_img = [heart_img, vacinne_img]


#>>>>>> HOME FRAME BUTTON <<<<<<#
start_btn = Button(home_frame, bd=10, image=button_start_img, command=start)
setting_btn = Button(
    home_frame, bd=10, image=button_setting_img, command=setting)
exit_btn = Button(home_frame, bd=10, image=button_exit_img, command=quit)
restart_btn_level1 = Button(
    root, bd=10, image=button_restart_img, command=restart_from_level_1)
restart_btn_level2 = Button(
    root, bd=10, image=button_restart_img, command=restart_from_level_2)
restart_btn_level3 = Button(
    root, bd=10, image=button_restart_img, command=restart_from_level_3)


#>>>>>> START FRAME BUTTON <<<<<<#
back_btn = Button(start_frame, bd=10, image=button_back_img, command=home)
level1_btn = Button(start_frame, bd=20,
                    image=button_level1_img, command=level_1)
level2_btn = Button(start_frame, bd=20,
                    image=button_level2_img, command=level_2)
level3_btn = Button(start_frame, bd=20,
                    image=button_level3_img, command=level_3)


############################################
#>>>>>> FUNCTIONS DEPLOYMENT HERE!!! <<<<<<#
############################################

home()

###########################
#>>>>>> KEY BINDING <<<<<<#
###########################

root.bind("<w>", move_up)
root.bind("<a>", move_left)
root.bind("<s>", move_down)
root.bind("<d>", move_right)
root.bind("<f>", upgrade)

root.mainloop()
