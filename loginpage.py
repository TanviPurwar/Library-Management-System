from tkinter import Tk
from tkinter import Label
from tkinter import Frame
from tkinter import Button
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import messagebox

class Login:
    
    def __init__(self, root, width, height):

        self.root = root
        self.width = width
        self.height = height

        self.root.title("Login Page")
        self.root.geometry(("%dx%d+0+0" % (width, height)))

        self.pic_frame = Frame(self.root)
        self.pic_frame.place(x = 0, y = 0, width = self.width-400, height = self.height)

        img1 = Image.open("./Images/loginpic.jpg")
        img1 = img1.resize((self.width-400, self.height), Image.ANTIALIAS)
        self.logo_img = ImageTk.PhotoImage(img1)

        pic_label = Label(self.pic_frame, image = self.logo_img, relief = 'flat')
        pic_label.place(x = 0, y = 0, width = self.width-400, height = self.height)

        self.login_frame = Frame(self.root, pady = 200, bg = '#0c5b83', padx = 80)
        self.login_frame.place(x = self.width-400, y = 0, width = 400, height = self.height)

        textlabel  = Label(self.login_frame, text = "Login to Your Account", font = ('Palatino', 27, 'bold'), bg = '#0c5b83', fg = '#d6d8d7')
        textlabel.place(x = -60, y = -100)

        self.usernameVar = StringVar()

        username_label = Label(self.login_frame, text  = "Username: ", font = ('Arial', 13, 'bold'), bg = '#0c5b83', fg = 'white', width = 10, anchor = 'w')
        username_label.grid(row = 0, column = 0, pady = 5, sticky = 'w')

        username_entry = ttk.Entry(self.login_frame, width = 25, font = ('Arial', 13), textvariable = self.usernameVar)
        username_entry.grid(row = 1, column = 0, pady = 5)

        self.passwordVar = StringVar()

        password_label = Label(self.login_frame, text  = "Password: ", font = ('Arial', 13, 'bold'), bg = '#0c5b83', fg = 'white', width = 10, anchor = 'w')
        password_label.grid(row = 2, column = 0, pady = 5, sticky = 'w')

        password_entry = ttk.Entry(self.login_frame, width = 25, font = ('Arial', 13), textvariable = self.passwordVar, show = '*')
        password_entry.grid(row = 3, column = 0, pady = 5)

        login_button = Button(self.login_frame, text = "Login", font = ('Arial', 13, 'bold'), bg = '#bcc3cc', fg = '#0c5b83', command = self.verify)
        login_button.grid(row = 4, column = 0, sticky = 'e', pady = 15)
    
    def verify(self):
        
        if str(self.usernameVar.get()) == 'Tanvi Purwar' and str(self.passwordVar.get()) == 'lms@555':
            print(self)
            self.login_frame.destroy()
            self.pic_frame.destroy()
            self.root.destroy()
        
        else:
            messagebox.showerror("Error", "Incorrect Login or Password")