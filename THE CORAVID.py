from tkinter import Button, Frame, PhotoImage, Tk, Canvas, mainloop, BOTH
from mechanism import *
import winsound 

 
################
### CONSTANT ###
################



WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_TITLE = "THE CORAVID"

GAME_ICON_LOCATION = ""
CHARACTER_IMG_LOCATION = ""
VIRUS_IMG_LOCATION = "Game_projects_group10\\assets\image\\b2.png"
CROSSHAIR = "Game_projects_group10\\assets\image\crosshairs.png"
ENEMY_IMG_LOCATION = "Game_projects_group10\\assets\image\\virus2.png"



BLACK_IMG_LOCATION="black_background.png"
BUTTON_START_IMG_LOCATION='button_start.png'
BUTTON_SETTING_IMG_LOCATION='button_setting.png'
BUTTON_EXIT_IMG_LOCATION='button_exit.png'
BUTTON_BACK_IMG_LOCATION='button_back.png'


BUTTON_LEVEL1_IMG_LOCATION='1.png'
BUTTON_LEVEL2_IMG_LOCATION='2.png'
BUTTON_LEVEL3_IMG_LOCATION='3.png'


BUTTON_ON_IMG_LOCATION='no.png'
BUTTON_OFF_IMG_LOCATION='off.png'

BACKGROUND_LEVEL1_LOCATION="level1.png"
BACKGROUND_LEVEL2_LOCATION="level2.png"
BACKGROUND_LEVEL3_LOCATION="level3.png"
BACKGROUND_START_LOCATION='wall.png'
SETTING_IMAGE_LOCATION='setting.png'



#################
### FOUCTION ####
#################

def home():
    lbl=main_canvas.create_image(500,300,image=mario)
    main_canvas.create_image(890,500,image=black1)
    button_start=main_canvas.create_image(890,430,image=start1,tags='button_start')
    button_setting=main_canvas.create_image(890,495,image=setting1,tags='button_setting')
    button_exit=main_canvas.create_image(890,560,image=exit1,tags='button_exit')


def start(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,300,image=background_start)
    main_canvas.create_image(70,40,image=back1,tags='text')
    button_level1 = main_canvas.create_image(300,300,image=one,tags='button_level1')
    button_level2 = main_canvas.create_image(550,300,image=two,tags='button_level2')
    button_level3 = main_canvas.create_image(800,300,image=three,tags='button_level3')

def setting(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,300,image=background_start)
    main_canvas.create_image(500,300,image=pic)
    main_canvas.create_image(70,40,image=back1,tags='text')
    
    sound_on = main_canvas.create_image(600,155,image=button_on,tags='button_on')
    sound_off = main_canvas.create_image(700,155,image=button_off,tags='button_off')
    music_on = main_canvas.create_image(600,250,image=button_on,tags='button_on')
    music_off = main_canvas.create_image(700,250,image=button_off,tags='button_off')

def back(event):
    home()


def level1(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,120,image=background_level1)
    main_canvas.create_image(70,560,image=back1,tags='text')
    
   

def level2(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,120,image=background_level2)
    main_canvas.create_image(70,560,image=back1,tags='text')




def level3(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,300,image=background_level3)
    main_canvas.create_image(70,560,image=back1,tags='text')



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


###### BACKGROUND ######
main_canvas.create_image(500,120,image=background_level1)


###### PLAYER CANVAS ######
player_canvas = main_canvas.create_oval(110,110, 150,150)


###### ENEMY ######
enemy = Enemy(root, main_canvas, enemy_img)
enemy.number_of_enemy(10)
enemy.move_enemy()

###### KEY BINDING ######

root.mainloop()
