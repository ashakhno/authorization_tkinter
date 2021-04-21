from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import argparse
import os


class AnimateGifLabel(Label):
    def __init__(self, *argv, image = None,  **kwargs):
        # self.master = argv[0]
        self.filename = image
        self.check_cadrs()
        self.i = 0
        self.img = Image.open(image)
        self.img.seek(0)
        self.image = ImageTk.PhotoImage(self.img)
        super().__init__(*argv, image=self.image, **kwargs)
        if 'delay' in kwargs:
            self.delay = kwargs['delay']
        else:
            try:
                self.delay = self.img.info['duration']
            except:
                self.delay = 100
        # self.delay = 3 # Minimal delay
        self.after(self.delay, self.show_new_cadr)

    def check_cadrs(self):
        self.cadrs = Image.open(self.filename).n_frames

    def show_new_cadr(self):
        if self.i == self.cadrs:
            self.i = 0
        self.img.seek(self.i)
        self.image = ImageTk.PhotoImage(self.img)
        self.config(image=self.image)
        self.i += 1
        self.master.after(self.delay, self.show_new_cadr)


root = Tk()


def click_restore():
    os.startfile(paths[password], 'open')


def click_father():
    os.startfile('father.jpg', 'open')


def click_music():
    os.startfile('track.mp3', 'open')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-p', '--password', default='', help='First file for teams')
args = vars(parser.parse_args())
password = args['password']
pwd = os.path.abspath(os.getcwd())
paths = {'ghfdlf?': os.path.join(pwd, 'disclosure_1.txt'),
         'hfcgkfnf1': os.path.join(pwd, 'disclosure_2.txt'),
         'dkfcnm775': os.path.join(pwd, 'disclosure_3.txt'),
         'ctvmz921': os.path.join(pwd, 'disclosure_4.txt'),
         ';bpym146': os.path.join(pwd, 'disclosure_5.txt')}


root.attributes('-fullscreen', True)
root.geometry('1920x1080')
root["bg"] = "black"
canvas = Canvas(root, width=1920,height=1080)
image = AnimateGifLabel(image="hack_gif.gif")

canvas.create_window(0, 0, anchor=NW, window=image)
canvas.pack()

# First string left
first_string_left = tk.Label(root, text="root@personal-pc~/root>", background="black", fg="green", font=("Calibri", 15))
first_string_left.place(x=225, y=60, anchor='center')

# First string right
first_string_right = tk.Label(root, text="whoami", background="black", fg="green", font=("Calibri", 15))
first_string_right.place(x=375, y=60, anchor='center')

# Second string
second_string_right = tk.Label(root, text="ArtMaster", background="black", fg="green", font=("Calibri", 15))
second_string_right.place(x=160, y=90, anchor='center')

# Third string left
third_string_left = tk.Label(root, text="root@personal-pc~/root>", background="black", fg="green", font=("Calibri", 15))
third_string_left.place(x=225, y=120, anchor='center')

# Third string right
third_string_right = tk.Label(root, text="rm -rf disclosure.txt", background="black", fg="green", font=("Calibri", 15))
third_string_right.place(x=430, y=120, anchor='center')

# Fourth string left
fourth_string_left = tk.Label(root, text="root@personal-pc~/root>", background="black", fg="green", font=("Calibri", 15))
fourth_string_left.place(x=225, y=150, anchor='center')

# Fourth string right
fourth_string_right = tk.Label(root, text="ls", background="black", fg="green", font=("Calibri", 15))
fourth_string_right.place(x=350, y=150, anchor='center')

# Fifth string
fifth_string_1 = tk.Label(root, text="matan_laba.py", background="black", fg="green", font=("Calibri", 15))
fifth_string_1.place(x=179, y=180, anchor='center')
fifth_string_2 = tk.Label(root, text="father.jpg", background="black", fg="green", font=("Calibri", 15))
fifth_string_2.place(x=300, y=180, anchor='center')
fifth_string_3 = tk.Label(root, text="track.mp3", background="black", fg="green", font=("Calibri", 15))
fifth_string_3.place(x=395, y=180, anchor='center')

restore = tk.Button(root, text="Restore file", command=click_restore, width=20, background="red")
restore.place(x=335, y=396, anchor='center')

father = tk.Button(root, text="Open father.jpg", command=click_father, width=17, background="red")
father.place(x=185, y=396, anchor='center')

music = tk.Button(root, text="Open track.mp3", command=click_music, width=17, background="red")
music.place(x=480, y=396, anchor='center')

root.mainloop()