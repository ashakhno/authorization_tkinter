from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import argparse
import os

class AnimateGifLabel(Label):
    def __init__(self, *argv, image = None,  **kwargs):
        #self.master = argv[0]
        self.filename = image
        self.check_cadrs()
        self.i = 0
        self.img = Image.open(image)
        self.img.seek(0)
        self.image = ImageTk.PhotoImage(self.img)
        super().__init__(*argv, image = self.image, **kwargs)
        if 'delay' in kwargs:
            self.delay = kwargs['delay']
        else:
            try:
                self.delay = self.img.info['duration']
            except:
                self.delay = 100
        #self.delay = 3 # Это минимально возможная задержка - иначе ткинтер не успевает обновится и не обновляет 2  (Но реагирует на события типа изменнения размера ) а при 1 даже не появляется
        self.after(self.delay, self.show_new_cadr)


    def check_cadrs(self):
        self.cadrs = Image.open(self.filename).n_frames
    def show_new_cadr(self):
        if self.i == self.cadrs:
            self.i=0
        self.img.seek(self.i)
        self.image = ImageTk.PhotoImage(self.img)
        self.config(image = self.image)
        self.i+=1
        self.master.after(self.delay, self.show_new_cadr)
root=Tk()


def click_restore():
    os.startfile(paths[password], 'open')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-p', '--password', default='', help='First file for teams')
args = vars(parser.parse_args())
password = args['password']
pwd = os.path.abspath(os.getcwd())
paths = {'ghfdlf?': os.path.join(pwd, 'secret_file_1.txt'),
         'hfcgkfnf1': os.path.join(pwd, 'secret_file_2.txt'),
         'dkfcnm775': os.path.join(pwd, 'secret_file_3.txt'),
         'ctvmz921': os.path.join(pwd, 'secret_file_4.txt'),
         ';bpym146': os.path.join(pwd, 'secret_file_5.txt')}


root.attributes('-fullscreen', True)
root.geometry('1920x1080')
root["bg"] = "black"
canvas=Canvas(root,width=1920,height=1080)
image=AnimateGifLabel(image="hack_gif.gif")

canvas.create_window(0,0,anchor=NW,window=image)
canvas.pack()
first_string = tk.Label(root, text="root@personal-pc~/root>", background="black",fg="green", font=("Calibri", 15))
first_string.place(x=225, y=60, anchor='center')

restore = tk.Button(root, text="Restore file", command=click_restore, width=20, background="red")
restore.place(x=330, y=396, anchor='center')

root.mainloop()