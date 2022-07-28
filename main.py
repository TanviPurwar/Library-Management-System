from tkinter import Tk
from tkinter import Label
from tkinter import Frame
from tkinter import Button
from PIL import Image, ImageTk
from books import Books
from loginpage import Login

class LibraryManagementSystem:

    def disable_btns(self, frame): #disabling menu buttons  
        for widget in frame.winfo_children():
            widget["state"] = 'disabled'

    def __init__(self, root, height, width):
        #giving width and height of screen
        self.width = width
        self.height = height

        #setting title and geometry of root window 
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry(("%dx%d+0+0" % (width, height)))

        #loading, resizing and scaling images
        img1 = Image.open("./Images/booknpencil.png")
        img1 = img1.resize((200, 200), Image.ANTIALIAS)
        self.logo_img = ImageTk.PhotoImage(img1)

        #putting images on labels to put on screen
        logo_label = Label(self.root, image = self.logo_img, relief = 'flat')
        logo_label.place(x = 0, y = 0, width = 200, height = 200)

        #Setting Title
        title_label = Label(self.root, text = "Library Management System", font = ("Palatino", 40, "bold"), bg = "#E6D8CE", fg="#736962")
        title_label.place(x = 200, y = 0, width = self.width-200, height = 85)

        #menu frame
        menu_label = Label(self.root, text = "Menu", bd=2, relief = 'ridge', font = ("Palatino", 25, "bold"), bg = "#E6D8CE", fg = "#736962")
        menu_label.place(x = 0, y = 200, width = 200, height = 50)

        self.menu_frame = Frame(self.root, bd=2, relief = 'ridge', bg = "white")
        self.menu_frame.place(x = 0, y = 250, width = 200, height = self.height-250)

        #menu buttons
        issue_books = Button(self.menu_frame, text = "Issue Books", width = 200, bd=3, relief = 'raised', font = ("Palatino", 15, "bold"), bg = "#40B7AD", fg="white", command=self.issue_bk).pack()
        return_books = Button(self.menu_frame, text = "Return Books", width = 200, bd=3, relief = 'raised', font = ("Palatino", 15, "bold"), bg = "#40B7AD", fg="white", command=self.return_bk).pack()
        book_menu = Button(self.menu_frame, text = "Book", width = 200, bd=3, relief = 'raised', font = ("Palatino", 15, "bold"), bg = "#40B7AD", fg="white", command=self.book).pack()
        member_menu= Button(self.menu_frame, text = "Members", width = 200, bd=3, relief = 'raised', font = ("Palatino", 15, "bold"), bg = "#40B7AD", fg="white", command=self.member).pack()
        download_reports = Button(self.menu_frame, text = "Reports", width = 200, bd=3, relief = 'raised', font = ("Palatino", 15, "bold"), bg = "#40B7AD", fg="white", command=self.report).pack()

        #main frame
        self.main_frame = Frame(self.root, bd=2, relief = 'ridge', bg = "#dbfdff", pady = 70)
        self.main_frame.place(x = 200, y = 85, width = self.width-200, height = self.height-85)
    
    def issue_bk(self):
        self.disable_btns(self.menu_frame)
        obj = Books(self.root, self.main_frame, self.menu_frame, self.width-200, self.height-85)
        obj.issue_book()
        #print(self.main_frame.winfo_children())
    
    def return_bk(self):
        self.disable_btns(self.menu_frame)
        obj = Books(self.root, self.main_frame, self.menu_frame, self.width-200, self.height-85)
        obj.return_book()
    
    def book(self):
        self.disable_btns(self.menu_frame)
        obj = Books(self.root, self.main_frame, self.menu_frame, self.width-200, self.height-85)
        obj.book_fn()
    
    def member(self):
        self.disable_btns(self.menu_frame)
        obj = Books(self.root, self.main_frame, self.menu_frame, self.width-200, self.height-85)
        obj.member_fn()

    def report(self):
        self.disable_btns(self.menu_frame)
        obj = Books(self.root, self.main_frame, self.menu_frame, self.width-200, self.height-85)
        obj.reports()

if __name__ == "__main__":

    root = Tk()
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()

    login_obj = Login(root, width, height)
    root.mainloop()
    
    root = Tk()
    main_obj = LibraryManagementSystem(root, height, width)
    root.mainloop()

    

#Image by <a href="https://pixabay.com/users/memed_nurrohmad-3307648/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2389229">Memed_Nurrohmad</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2389229">Pixabay</a>