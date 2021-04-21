import argparse
import tkinter as tk
import os


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-p', '--password', default='', help='First file for teams')
args = vars(parser.parse_args())
password = args['password']
paths = {'ghfdlf?': r'C:\Users\ashakhnov\PycharmProjects\terminal_for_InTeam\secret_file_1.txt',
         'hfcgkfnf1': r'C:\Users\ashakhnov\PycharmProjects\terminal_for_InTeam\secret_file_2.txt',
         'dkfcnm775': r'C:\Users\ashakhnov\PycharmProjects\terminal_for_InTeam\secret_file_3.txt',
         'ctvmz921': r'C:\Users\ashakhnov\PycharmProjects\terminal_for_InTeam\secret_file_4.txt',
         ';bpym146': r'C:\Users\ashakhnov\PycharmProjects\terminal_for_InTeam\secret_file_5.txt'}

class Database:
    def __init__(self):
        self.window = tk.Tk()
        self.window["bg"] = "gray"
        self.window.title("Database")
        self.window.attributes('-fullscreen', True)
        self.window.geometry('1920x1200')
        self.fullScreenState = False
        self.first_string = tk.Label(self.window, text="master@personal-pc~/root>", background="gray", font=("Calibri", 25))
        self.first_string.place(x=200, y=20, anchor='center')
        self.second_string = tk.Label(self.window, text="Какая-то ненужная информация", background="gray", font=("Calibri", 25))
        self.second_string.place(x=650, y=20, anchor='center')
        self.third_string = tk.Label(self.window, text="master@personal-pc~/root> cd /root/doc/secret_file.txt", background="gray", font=("Calibri", 25))
        self.third_string.place(x=388, y=60, anchor='center')
        self.fourth_string = tk.Label(self.window, text="Закидаю и оформлю красиво всё короче завтра", background="gray", font=("Calibri", 25))
        self.fourth_string.place(x=700, y=600, anchor='center')
        self.restore = tk.Button(self.window, text="Restore file", command=self.click_restore, width=20)
        self.restore.place(x=1500, y=650, anchor='center')
        """self.username = tk.Label(self.window, text="User", background="gray", font=("Calibri", 25))
        self.username.place(x=800, y=498, anchor='center')
        self.username_entry = tk.StringVar()
        self.username_text = tk.Entry(self.window, textvariable=self.username_entry, width=30, bd=5)
        self.username_text.place(x=930, y=500, anchor='center')
        self.password = tk.Label(self.window, text="Password", background="gray", font=("Calibri", 25))
        self.password.place(x=760, y=560, anchor='center')
        self.password_entry = tk.StringVar()
        self.password_text = tk.Entry(self.window, textvariable=self.password_entry, width=30, bd=5, show='*')
        self.password_text.place(x=930, y=560, anchor='center')
        self.login = tk.Button(self.window, text="Log in", command=self.click_login, width=20)
        self.login.place(x=930, y=650, anchor='center')"""

        self.window.mainloop()

    def click_restore(self):

        os.startfile(paths[password], 'open')

if __name__ == '__main__':
    app = Database()