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
    button_level1=main_canvas.create_image(300,300,image=one,tags='button_level1')
    button_level2=main_canvas.create_image(550,300,image=two,tags='button_level2')
    button_level3=main_canvas.create_image(800,300,image=three,tags='button_level3')

def setting(event):
    main_canvas.delete('all')
    main_canvas.create_image(500,300,image=background_start)
    main_canvas.create_image(500,300,image=pic)
    main_canvas.create_image(70,40,image=back1,tags='text')
    
    sound_on=main_canvas.create_image(600,155,image=button_on,tags='button_on')
    sound_off=main_canvas.create_image(700,155,image=button_off,tags='button_off')
    music_on=main_canvas.create_image(600,250,image=button_on,tags='button_on')
    music_off=main_canvas.create_image(700,250,image=button_off,tags='button_off')


def quit(event):
    root.destroy()

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

    
# def Deplaymusic(event):
    















#################
### MAIN CODE ###
#################


###### GUI WINDOWS INTERFACE ######
root = Tk()
root.title(GAME_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(0,0)


#########################
######## Back############
#########################

    


###### MAIN CANVAS ######
main_canvas = Canvas(root)
main_canvas.pack(expand=True, fill=BOTH)

background_level1=PhotoImage(file="Game_projects_group10\\assets\image\LEVEL1.png")
main_canvas.create_image(500,120,image=background_level1)

###### PLAYER CANVAS ######
player_canvas = main_canvas.create_oval(110,110, 150,150)
player_crosshair = PhotoImage(file=CROSSHAIR)

###### PLAYER FUNTION ######
main_player = Movements(root, main_canvas, player_canvas)

###### ENEMY
enemy_img = PhotoImage(file=ENEMY_IMG_LOCATION)
enemy = Enemy(root, main_canvas, enemy_img)
enemy.number_of_enemy(10)
enemy.enem_dictionary()
enemy.move_enemy()
root.bind("<Motion>", main_player.aim)
main_player.crosshair(player_crosshair)


#####################
##### BUTTON ########
########3############

main_canvas.tag_bind("button_start","<Button-1>", start)
main_canvas.tag_bind("button_setting","<Button-1>", setting)
main_canvas.tag_bind("button_exit","<Button-1>", quit)
main_canvas.tag_bind("text","<Button-1>", back)
main_canvas.tag_bind("button_level1","<Button-1>", level1)
main_canvas.tag_bind("button_level2","<Button-1>", level2)
main_canvas.tag_bind("button_level3","<Button-1>", level3)

##############################
#### BACKGROUND IMAGES########
##############################

background_level1=PhotoImage(file="level1.png")
background_level2=PhotoImage(file="level2.png")
background_level3=PhotoImage(file="level3.png")
background_start=PhotoImage(file='wall.png')
pic=PhotoImage(file='setting.png')

#############################
######## BUTTTON IMAGES######
#############################

black1=PhotoImage(file="12345.png")
start1=PhotoImage(file='button_start.png')
setting1=PhotoImage(file='button_setting.png')
exit1=PhotoImage(file='button_exit.png')
back1=PhotoImage(file='button_back.png')

button_on=PhotoImage(file='no.png')
button_off=PhotoImage(file='off.png')

one=PhotoImage(file='1.png')
two=PhotoImage(file='2.png')
three=PhotoImage(file='3.png')

###########################
####### SOUND #############
###########################
music=winsound.PlaySound("Pirates.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )



######## CALL FUNCATION HOME#####
home()

###### PLAYER KEY BIND ######
root.bind("<w>", main_player.move_up)
root.bind("<a>", main_player.move_left)
root.bind("<s>", main_player.move_down)
root.bind("<d>", main_player.move_right)


root.mainloop()
