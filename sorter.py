from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
from os import *


# initialize Tk app
root = Tk()
root.title("Easy Image Sorter")
root.geometry("800x800")

# get directory path and create queue
path = askdirectory(title="Select folder")
dir_list = listdir(path)
image_list = []
for item in dir_list:
    name = item
    if ".png" in name:
        image_list.append(item)

# text_output = Text(root, height=10, width=60)
# text_output.grid(row=1, column=0, padx=175)
#
# for item in image_list:
#     text_output.insert(END, item + "\n")

# pull first image
image_path = image_list.pop()
show_image = Image.open(path + "/" + image_path)
show_image.thumbnail((500, 500), Image.LANCZOS)
show_image = ImageTk.PhotoImage(show_image)

Label(image=show_image).grid(row=0, column=0, padx=175, pady=50)


# button functionality to sort by folder

# display image and buttons
# test_image = Image.open("C:/Users/US7058/Pictures/Photos/test1.png")
# test_image.thumbnail((500, 500), Image.LANCZOS)
# test_image = ImageTk.PhotoImage(test_image)
#
# Label(image=test_image).grid(row=0, column=0, padx=175, pady=50)
Button(root, text="Exit", command=root.quit).grid(row=2, column=0)

root.mainloop()
