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
        self.sort_folders = []
        self.image_list = []
        self.current_index = 0
        self.amount_of_folders_chosen = 0

        # create GUI
        self.create_homepage()

    def create_homepage(self):
        """builds the welcome page of the program"""
        # display homepage text
        self.welcome_label = tk.Label(self.master, text="Welcome to the Easy Image Sorter!")
        self.welcome_label.pack(pady=(20, 0))

        # display homepage image
        self.start_label = tk.Label(self.master)
        self.start_label.pack(expand=True)
        start_image_path = 'homepage.png'
        start = Image.open(start_image_path)
        start.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(start)
        self.start_label.config(image=photo)
        self.start_label.image = photo

        # display homepage text
        self.welcome_label2 = tk.Label(self.master, text="Please select a folder to begin sorting.")
        self.welcome_label2.pack(pady=(0, 20))

        # display main folder button
        self.main_folder_button = tk.Button(text="Select folder", command=self.select_main)
        self.main_folder_button.pack(pady=(0, 10))

    def create_display(self):
        """selects buttons for sort folders and builds the display for images"""
        self.how_many = tk.Label(self.master, text="How many sorting folders will you need?")
        self.how_many.pack()
        self.amount_of_folders = tk.Entry(self.master)
        self.amount_of_folders.pack()
        self.submit = tk.Button(self.master, text="Select folders", command=self.select_sub)
        self.submit.pack()

    def select_main(self):
        """selects the main starting folder"""
        self.main_folder = filedialog.askdirectory(title="Select start folder")
        self.start_label.pack_forget()
        self.welcome_label2.pack_forget()
        self.main_folder_button.pack_forget()

        self.main_folder_label = tk.Label(self.master, text=f"You selected {self.main_folder}.")
        self.main_folder_label.pack(side=tk.TOP, pady=(50, 0))
        self.retry_button = tk.Button(self.master, text="RETRY", command=self.restart)
        self.retry_button.pack()
        self.cont_button = tk.Button(self.master, text="CONTINUE", command=self.create_display)
        self.cont_button.pack()

    def select_sub(self):
        """selects subfolders for sorting"""
        self.sort_folders_button = tk.Button(text="Select sort folders")

    def restart(self):
        """clears widgets and restarts home screen"""
        self.welcome_label.pack_forget()
        self.main_folder_label.pack_forget()
        self.retry_button.pack_forget()
        self.cont_button.pack_forget()
        self.create_homepage()

    #     # TODO maybe i need to move the below to a new function?
    #
    #     # select sub-folders
    #     # self.sort_folders_button = tk.Button(text="Select sort folders")
    #     for i in range(self.amount_of_folders_chosen):
    #         self.sort_folders[i] = filedialog.askdirectory(title=f"Select folder for button {i + 1}")

        # self.create_list()
        # self.display_page()

    # def display_page(self):
    #     """displays images after all folders are chosen"""
    #     # image label
    #     self.image_label = tk.Label(self.master)
    #     self.image_label.pack(expand=True)
    #
    #     # 'no more images' label at end of the list
    #     self.no_more_label = tk.Label(self.master, text="No more images. Please select a new folder.")
    #
    #     # anchor buttons at bottom of window using a frame
    #     button_frame = tk.Frame(self.master)
    #     button_frame.pack(side=tk.BOTTOM, pady=(0, 20))
    #
    #     # create buttons to sort folders
    #     for i in range(self.amount_of_folders_chosen):
    #         btn = tk.Button(button_frame, text=f"{self.sort_folders[i]}", command=lambda idx=i: self.move_image(idx))
    #         btn.pack(side=tk.LEFT)  # TODO what does this do?
    #         self.master.bind(str(i + 1), lambda event, idx=i: self.move_image(idx))
    #
    #     skip_button = tk.Button(button_frame, text="SKIP", command=self.next_image)
    #     skip_button.pack(side=tk.LEFT)  # TODO what does this do?
    #     self.master.bind(str(len(self.sort_folders) + 1), lambda event: self.next_image())
    #
    #     # self.load_image()
    #
    def get_input(self):
        """gets and stores user input"""
        user_input = self.amount_of_folders.get()
        self.amount_of_folders_chosen = int(user_input)
        self.how_many.pack_forget()
        self.amount_of_folders.pack_forget()
        self.submit.pack_forget()
    #
    # def create_list(self):
    #     """creates the image list"""
    #     # load image list and display first image
    #     self.image_list = [f for f in os.listdir(self.main_folder) if
    #                        f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    #     self.current_index = 0
    #
    # def load_image(self):
    #     """loads the image to be displayed and displays it"""
    #     if self.current_index < len(self.image_list):
    #         image_path = os.path.join(self.main_folder, self.image_list[self.current_index])
    #         image = Image.open(image_path)
    #         image.thumbnail((400, 400))
    #         photo = ImageTk.PhotoImage(image)
    #         self.image_label.config(image=photo)
    #         self.image_label.image = photo
    #         self.no_more_label.pack_forget()
    #     else:
    #         self.no_more_label.pack()
    #
    # def move_image(self):
    #     """moves image to new location based on button press"""
    #     pass
    #
    # def next_image(self):
    #     """moves to the next image in the list"""
    #     pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSorterApp(root)
    root.mainloop()
