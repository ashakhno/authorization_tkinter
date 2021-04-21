import tkinter as tk
from tkinter import messagebox
import subprocess



class Authorization:
    def __init__(self):
        self.window = tk.Tk()
        self.window["bg"] = "gray"
        self.window.title("Terminal")
        self.window.attributes('-fullscreen', True)
        self.window.geometry('1920x1200')
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.username = tk.Label(self.window, text="User", background="gray", font=("Calibri", 25))
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
        self.login.place(x=930, y=650, anchor='center')
        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def click_login(self):
        login = "master"
        passwords = ['ghfdlf?', 'hfcgkfnf1', 'dkfcnm775', 'ctvmz921', ';bpym146']
        database = r'C:\Users\ashakhnov\PycharmProjects\terminal_for_InTeam\progress_bar.py'
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        if entered_username == login and entered_password in passwords:
            messagebox.showinfo('Log In', 'Success')
            command = ['python', database, '-p', entered_password]
            subprocess.Popen(command)
        else:
            messagebox.showinfo('Authorization failed', 'Incorrect login or password')


if __name__ == '__main__':
    app = Authorization()