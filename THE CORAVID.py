from tkinter import Button, Frame, PhotoImage, Tk, Canvas, mainloop, BOTH
from library.mechanism import *
from library.constant import * 
import winsound 

#################
### FOUCTION ####
#################
########################################################################
def key_bind():
    root.bind("<w>", player.move_up)
    root.bind("<a>", player.move_left)
    root.bind("<s>", player.move_down)
    root.bind("<d>", player.move_right)
    root.bind("<Motion>", player.aim)

def deploy_sprite(enemy_count:int, player_pos:list):
    enemy = Enemy(root, main_canvas, enemy_img)
    enemy.move_enemy()
    enemy.number_of_enemy(enemy_count)
    deploy_character(player_pos[0], player_pos[1], 20, None)
    key_bind()

def home():
    main_canvas.delete('all')
    main_canvas.create_image(500,300,image=background_home_img)
    main_canvas.create_image(890,500,image=background_black_img)
    button_start=main_canvas.create_image(890,430,image=button_start_img,tags='button_start')
    button_setting=main_canvas.create_image(890,495,image=button_setting_img,tags='button_setting')
    button_exit=main_canvas.create_image(890,560,image=button_exit_img,tags='button_exit')

def start(event):

    winsound.PlaySound(MUSIC_CHOICE,winsound.SND_FILENAME | winsound.SND_ASYNC )
    main_canvas.create_image(500,300,image=background_start_img)
    main_canvas.create_image(70,40,image=button_back_img,tags='text')
    button_level1 = main_canvas.create_image(200,300,image=button_level1_img,tags='button_level1')
    button_level2 = main_canvas.create_image(500,300,image=button_level2_img,tags='button_level2')
    button_level3 = main_canvas.create_image(800,300,image=button_level3_img,tags='button_level3')

def setting(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,300,image=background_start_img)
    main_canvas.create_image(500,300,image=background_setting_img)
    main_canvas.create_image(70,40,image=button_back_img,tags='text')
    
    sound_on = main_canvas.create_image(600,155,image=button_on_img,tags='button_on')
    sound_off = main_canvas.create_image(700,155,image=button_off_img,tags='button_off')
    music_on = main_canvas.create_image(600,250,image=button_on_img,tags='button_on')
    music_off = main_canvas.create_image(700,250,image=button_off_img,tags='button_off')

def back(event):
    home()

def level1(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,120,image=background_level1)
    main_canvas.create_image(70,560,image=button_back_img,tags='text')
    deploy_sprite(10, [150,150])

def level2(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,120,image=background_level2_img)
    main_canvas.create_image(70,560,image=button_back_img,tags='text')

def level3(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,300,image=background_level3_img)
    main_canvas.create_image(70,560,image=button_back_img,tags='text')






########################################################################

def deploy_character( poxX:float, posY:float, player_size:int, image=None):
    global player
    player_box = main_canvas.create_oval(poxX, posY, poxX + player_size, posY + player_size)
    mid_point = main_canvas.coords(player_box)
    player = Player(main_canvas, player_box, player_crosshair)
    player.crosshair(player_crosshair)




#################
### MAIN CODE ###
#################

###### GUI WINDOWS INTERFACE ######
root = Tk()
root.title(GAME_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(0,0)


###### MAIN CANVAS ######
main_canvas = Canvas(root)
main_canvas.pack(expand=True, fill=BOTH)


###### PhotoImage ######
background_level1=PhotoImage(file="Game_projects_group10\\assets\image\LEVEL1.png")
player_crosshair = PhotoImage(file=CROSSHAIR)
enemy_img = PhotoImage(file=ENEMY_IMG_LOCATION)
#>>>>> BACKGROUND
background_home_img=PhotoImage(file=HOME_BACKGROUND_IMAGE_LOCATION)
background_black_img=PhotoImage(file=BLACK_IMG_LOCATION)
background_level1_img=PhotoImage(file=BACKGROUND_LEVEL1_LOCATION)
background_level2_img=PhotoImage(file=BACKGROUND_LEVEL2_LOCATION)
background_level3_img=PhotoImage(file=BACKGROUND_LEVEL3_LOCATION)
background_start_img=PhotoImage(file=BACKGROUND_START_LOCATION)
background_setting_img=PhotoImage(file=SETTING_IMAGE_LOCATION)
#>>>>> BUTTON
button_start_img =PhotoImage(file=BUTTON_START_IMG_LOCATION)
button_setting_img=PhotoImage(file=BUTTON_SETTING_IMG_LOCATION)
button_exit_img=PhotoImage(file=BUTTON_EXIT_IMG_LOCATION)
button_back_img=PhotoImage(file=BUTTON_BACK_IMG_LOCATION)
button_level1_img=PhotoImage(file=BUTTON_LEVEL1_IMG_LOCATION)
button_level2_img=PhotoImage(file=BUTTON_LEVEL2_IMG_LOCATION)
button_level3_img=PhotoImage(file=BUTTON_LEVEL3_IMG_LOCATION)
button_on_img=PhotoImage(file=BUTTON_ON_IMG_LOCATION)
button_off_img=PhotoImage(file=BUTTON_OFF_IMG_LOCATION)



home()

###### ENEMY ######

# enemy = Enemy(root, main_canvas, enemy_img)
# enemy.number_of_enemy(10)
# enemy.move_enemy()

###### KEY BINDING ######
#>>> PLAYER

#>>> SHAPE BIND
main_canvas.tag_bind("button_start","<Button-1>", start)
main_canvas.tag_bind("button_setting","<Button-1>", setting)
main_canvas.tag_bind("button_exit","<Button-1>", quit)
main_canvas.tag_bind("text","<Button-1>", back)
main_canvas.tag_bind("button_level1","<Button-1>", level1)
main_canvas.tag_bind("button_level2","<Button-1>", level2)
main_canvas.tag_bind("button_level3","<Button-1>", level3)




root.mainloop()
