from library.sprite import Items
from library.constant import *
from tkinter import *

item_dictionary = {}
item_data = {}

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
    
    o = canvas.gettags()
    print(o)
    return return_value


def move_right(event):
    movement(x=40)


def move_left(event):
    movement(x=-40)


def move_down(event):
    movement(y=40)


def move_up(event):
    movement(y=-40)

def build_item(item_data):
    for key in item_data:
        item_dictionary[key]=canvas.create_image(
            item_data[key]["position"], image=item_data[key]["img_location"],
            tags=item_data[key]["item"]
        )

def deploy_sprite():
    global player
    items = Items(item_data, item_img)
    items.generate_item_dict(10)
    build_item(item_data)
    print(item_dictionary)

    player = canvas.create_image(
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=player_img)

root = Tk()
root.geometry("800x600")


canvas = Canvas(root)
canvas.pack(expand=True, fill=BOTH)

player_img = PhotoImage(file=CHARACTER_IMG_LOCATION)


green_virus_img = PhotoImage(file=GREEN_VIRUS_LOCATION)
heart_img = PhotoImage(file=HEART_LOCATION)
red_virus_img = PhotoImage(file=RED_VIRUS_LOCATION)
vacinne_img = PhotoImage(file=VACINNE_LOCATION)
blood_img = PhotoImage(file=BLOOD_LOCATION)

item_img = [green_virus_img, heart_img, red_virus_img, vacinne_img, blood_img]




deploy_sprite()



root.bind("<w>", move_up)
root.bind("<a>", move_left)
root.bind("<s>", move_down)
root.bind("<d>", move_right)

root.mainloop()