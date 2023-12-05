import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageSorterApp:
    def __init__(self, master):
        self.master = master  # create root, and create new instance of class with ImageSorterApp(root)
        self.master.title("Easy Image Sorter")  # title will display at the top of the app
        self.master.geometry("600x600")  # set the window size to be fixed, so things stay clean and don't move around

        # initialize variables
        self.main_folder = ''
        self.sort_folders = ['', '', '', '']  # TODO update to take user input for number of folders
        self.image_list = []  # will store image list from main_folder
        self.current_index = 0  # index to start iterating through the list

        # create GUI
        self.create_widgets()  # will run create_widgets as defined below

    def create_widgets(self):
        """creates tkinter widgets to display in the master window"""
        # image label
        self.image_label = tk.Label(self.master)
        self.image_label.pack(expand=True)  # pack the image label, and expand to fill space

        # 'no more images' label at end of the list
        self.end_images_label = tk.Label(self.master, text="No more images. Please select a new folder.")
        self.end_images_label.pack()  # add the label in to the window
        self.end_images_label.pack_forget()  # hide label initially as it isn't needed until later

        # anchor buttons at the bottom of the window using a frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(side=tk.BOTTOM)  # TODO add padding between buttons

        # create buttons for sorting folders
        select_folders_button = tk.Button(button_frame, text="Select folders", command=self.select_folders)
        select_folders_button.pack(side=tk.TOP)  # TODO add padding between buttons

        for i in range(4):  # TODO update to take user input for number of folders
            btn = tk.Button(button_frame, text=f"Move to folder {i + 1}", command=lambda idx=i: self.move_image(idx))
            # TODO update to show name of folders chosen
            btn.pack(side=tk.LEFT)
            # bind key presses
            self.master.bind(str(i + 1), lambda event, idx=i: self.move_image(idx))

        skip_btn = tk.Button(button_frame, text="SKIP", command=self.next_image)
        skip_btn.pack(side=tk.LEFT)
        self.master.bind("5", lambda event: self.next_image())

    def select_folders(self):
        """selects folders for main_folder and sort_folders"""
        self.main_folder = filedialog.askdirectory(title="Select main folder")
        for i in range(4):  # TODO update to have user input for number of folders
            self.sort_folders[i] = filedialog.askdirectory(title=f"Select folder for button {i+1}")

        # load image list and display first image
        self.image_list = [f for f in os.listdir(self.main_folder) if
                           f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        self.current_index = 0
        self.load_image()

        # show 'no more images' label when image list is complete
        self.end_images_label.pack_forget()

    def load_image(self):
        """loads the image to be displayed and displays it"""
        if self.current_index < len(self.image_list):
            image_path = os.path.join(self.main_folder, self.image_list[self.current_index])
            image = Image.open(image_path)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)  # TODO why is this here?
            self.image_label.image = photo
            self.end_images_label.pack_forget()
        else:
            self.end_images_label.pack()

    def move_image(self, folder_index):
        """moves the image to the specified folder based on its index in the folder list"""
        destination_folder = self.sort_folders[folder_index]
        current_image_path = os.path.join(self.main_folder, self.image_list[self.current_index])
        new_image_path = os.path.join(destination_folder, self.image_list[self.current_index])
        os.rename(current_image_path, new_image_path)
        self.next_image()

    def next_image(self):
        """moves to the next image in the list"""
        self.current_index += 1
        self.load_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSorterApp(root)
    root.mainloop()
