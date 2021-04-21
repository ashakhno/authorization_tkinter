from tkinter import *
import argparse
import tkinter.ttk as ttk
import time, threading
import subprocess

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-p', '--password', default='', help='Password of a team')
args = vars(parser.parse_args())
password = args['password']

root = Tk()
root["bg"] = "gray"
root.attributes('-fullscreen', True)
root.geometry('1920x1200')
pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
pb.place(x=830, y=600, )
pb.start()


database = r'C:\Users\ashakhnov\PycharmProjects\terminal_for_InTeam\database.py'


def progress():
    for i in range(20):
        pb['value'] += i
        time.sleep(.2)
        if i == 19:
            pb.stop()
            quit_window()


def quit_window():
    command = ['python', database, '-p', password]
    subprocess.Popen(command)
    root.quit()

threading.Thread(target=progress).start()
root.mainloop()