from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
from os import *


# initialize Tk app
root = Tk()
root.title("Easy Image Sorter")
root.geometry("600x600")


# get directory path and create list
path = askdirectory(title="Select folder")
dir_list = listdir(path)
image_list = []
for item in dir_list:
    name = item
    if ".png" in name:
        image_list.append(item)


# pull and process first image TODO make a function for this?
# image_path = image_list[0]
# show_image = Image.open(path + "/" + image_path)
# show_image.thumbnail((500, 500), Image.LANCZOS)
# show_image = ImageTk.PhotoImage(show_image)
image_path = image_list[0]
show_image = Image.open(path + "/" + image_path)
show_image = ImageTk.PhotoImage(show_image)


# create forward/back button functions
def forward(image_number):
    global image_label
    global button_forward
    global button_back

    image_label.grid_forget()
    # new_image = Image.open(path + "/" + image_list[image_number-1])
    # new_image.thumbnail((500, 500), Image.LANCZOS)
    # new_image = ImageTk.PhotoImage(new_image)
    # image_label = Label(image=new_image)
    # image_label.grid(row=0, column=0, columnspan=3, padx=25, pady=25)
    new_path = image_list[image_number - 1]
    new_image = Image.open(path + "/" + new_path)
    new_image = ImageTk.PhotoImage(new_image)
    image_label = Label(image=new_image)
    image_label.grid(row=0, column=0, columnspan=3, padx=25, pady=25)


def back():
    global image_label
    global button_forward
    global button_back


# define variables
image_label = Label(image=show_image)
button_back = Button(root, text="Back", command=back)
button_forward = Button(root, text="Forward", command=lambda: forward(2))
button_exit = Button(root, text="Exit", command=root.quit)


# display labels and buttons
image_label.grid(row=0, column=0, columnspan=3, padx=25, pady=25)
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
