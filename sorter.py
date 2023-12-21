import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from send2trash import send2trash


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
        self.main_folder_label.pack_forget()
        self.retry_button.pack_forget()
        self.cont_button.pack_forget()

        self.image_list = [f for f in os.listdir(self.main_folder) if
                           f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        self.current_index = 0

        self.how_many = tk.Label(self.master, text="How many sorting folders will you need?")
        self.how_many.pack(pady=(0, 15))
        self.amount_of_folders = tk.Entry(self.master)
        self.amount_of_folders.pack(pady=(0, 15))
        self.submit = tk.Button(self.master, text="Select folders", command=self.select_sub)
        self.submit.pack()

    def select_main(self):
        """selects the main starting folder"""
        self.main_folder = filedialog.askdirectory(title="Select start folder")
        self.start_label.pack_forget()
        self.welcome_label2.pack_forget()
        self.main_folder_button.pack_forget()

        self.main_folder_label = tk.Label(self.master, text=f"You selected {self.main_folder}.")
        self.main_folder_label.config(font=15)
        self.main_folder_label.pack(side=tk.TOP, pady=(50, 0))

        self.select_frame = tk.Frame(self.master)
        self.select_frame.pack(pady=15)
        self.cont_button = tk.Button(self.select_frame, text="CONTINUE", command=self.create_display)
        self.cont_button.pack(side=tk.LEFT, padx=20)
        self.retry_button = tk.Button(self.select_frame, text="RETRY", command=self.restart)
        self.retry_button.pack(side=tk.BOTTOM)

    def select_sub(self):
        """selects subfolders for sorting"""
        self.get_input()

        for i in range(self.amount_of_folders_chosen):
            folder = filedialog.askdirectory(title=f"Select sorting folder {i + 1}")
            self.sort_folders.append(folder)

        self.create_sort_screen()

    def create_sort_screen(self):
        """builds the widgets for the sort screen"""
        # image label
        self.image_label = tk.Label(self.master)
        self.image_label.pack(expand=True)

        # store sort buttons together
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=(0, 20))

        # create buttons for sorting folders
        for i in range(int(self.amount_of_folders_chosen)):
            folder_name = self.sort_folders[i]
            folder_name_start = folder_name.rindex("/")
            button_name = folder_name[(folder_name_start+1):]
            btn = tk.Button(self.button_frame, text=f"{button_name} ({i+1})",
                            command=lambda idx=i: self.move_image(idx))
            btn.pack(side=tk.LEFT, padx=5)
            self.master.bind(str(i+1), lambda event, idx=i: self.move_image(idx))  # bind keys

        # anchor trash, skip, and home buttons at the bottom
        self.command_frame = tk.Frame(self.master)
        self.command_frame.pack(side=tk.BOTTOM, pady=(5, 10))

        # create skip button
        self.skip_button = tk.Button(self.command_frame, text="SKIP (=)", command=self.next_image)
        self.skip_button.pack(side=tk.LEFT)
        self.master.bind("=", lambda event: self.next_image())

        self.trash_button = tk.Button(self.command_frame, text="TRASH (x)", command=self.move_to_trash)
        self.trash_button.pack(side=tk.BOTTOM, padx=5)
        self.master.bind("x", lambda event: self.move_to_trash())

        # TODO add select folders button

        self.load_image()

    def restart(self):
        """clears widgets and restarts home screen"""
        self.welcome_label.pack_forget()
        self.main_folder_label.pack_forget()
        self.retry_button.pack_forget()
        self.cont_button.pack_forget()
        self.create_homepage()

    def get_input(self):
        """gets and stores user input"""
        user_input = self.amount_of_folders.get()
        self.amount_of_folders_chosen = int(user_input)
        self.how_many.pack_forget()
        self.amount_of_folders.pack_forget()
        self.submit.pack_forget()

    def load_image(self):
        """loads the image to be displayed"""
        self.no_images_label = tk.Label(text="No more images. Please select a new folder.")
        if self.current_index < len(self.image_list):
            image_path = os.path.join(self.main_folder, self.image_list[self.current_index])
            image = Image.open(image_path)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            # self.no_images_label.pack_forget()
        else:
            self.welcome_label.pack_forget()
            self.image_label.pack_forget()
            self.button_frame.pack_forget()
            self.command_frame.pack_forget()
            self.master.unbind_all("<Key>")
            self.create_homepage()  # TODO add a return to home button

        # for i in range(int(self.amount_of_folders_chosen)):
        #             self.master.unbind(str(i + 1))
        #         self.master.unbind("=")
        #         self.master.unbind("x")

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

    def move_to_trash(self):
        """moves the current image to the trash"""
        if self.current_index < len(self.image_list):
            current_image_path = os.path.join(self.main_folder, self.image_list[self.current_index])
            current_image_path = current_image_path.replace("/", "\\")
            send2trash(current_image_path)
            self.next_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSorterApp(root)
    root.mainloop()
