from library.sprite import Items
from library.constant import *
from tkinter import *

item_dictionary = {}
item_data = {}


def build_item(item_data):
    for key in item_data:
        item_dictionary[key]=canvas.create_image(
            item_data[key]["position"], image=item_data[key]["img_location"]
        )

def deploy_sprite():

    
    items = Items(item_data, item_img)
    items.generate_item_dict(10)
    build_item(item_data)
    print(item_dictionary)


root = Tk()
root.geometry("800x600")


canvas = Canvas(root)
canvas.pack(expand=True, fill=BOTH)


green_virus_img = PhotoImage(file=GREEN_VIRUS_LOCATION)
heart_img = PhotoImage(file=HEART_LOCATION)
red_virus_img = PhotoImage(file=RED_VIRUS_LOCATION)
vacinne_img = PhotoImage(file=VACINNE_LOCATION)
blood_img = PhotoImage(file=BLOOD_LOCATION)

item_img = [green_virus_img, heart_img, red_virus_img, vacinne_img, blood_img]




deploy_sprite()




root.mainloop()