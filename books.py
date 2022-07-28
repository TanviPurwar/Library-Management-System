from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Frame
from tkinter import ttk
from tkinter import StringVar
import datetime
from tkcalendar import DateEntry
from data_management import Data

class Books:
    
    def delete_obj(self):
        #print(self)
        #print(self.d)

        #enable buttons
        for widget in self.menu.winfo_children():
            widget["state"] = 'normal'

        for widget in self.frame.winfo_children():
            widget.destroy()
        
        del self.d
        del self
        
        print("objects deleted")

        #print(self)

    def __init__(self, root, frame, menu, width, height):
        print(self)
        
        self.root = root
        self.frame = frame
        self.menu = menu

        self.width = width
        self.height = height

        self.close_button = Button(self.frame, text = "X", font = ("arial", 10 ,"bold"), bd=2, relief = "raised", bg = "red", fg = "white", command=self.delete_obj)
        self.close_button.place(x = self.width-25-0, y = 0-70, width = 25, height = 25)

        self.d = Data(self.frame)

    def display_data(self, dataTable, headers):

        #scrollbar
        scroll_x = ttk.Scrollbar(dataTable, orient = 'horizontal')
        scroll_y = ttk.Scrollbar(dataTable, orient = 'vertical')

        scroll_x.pack(side = 'bottom', fill = 'x')
        scroll_y.pack(side = 'right', fill = 'y')

        self.data_preview = ttk.Treeview(dataTable, column = headers, xscrollcommand = scroll_x, yscrollcommand = scroll_y)
        
        #config
        scroll_x.config(command = self.data_preview.xview)
        scroll_y.config(command = self.data_preview.yview)

        #show headings
        for i in range(0, len(headers)):
            self.data_preview.heading(headers[i], text = str(headers[i]))
        
        self.data_preview["show"] = "headings"

        for i in range(0, len(headers)):
            self.data_preview.column(headers[i], width = 100)

        self.data_preview.pack(fill = 'both', expand = 1)


    def issue_book(self):

        #create form
        issue_list = ["Register No", "Name", "Book Id", "Title", "Author", "ISBN", "Date of Issue", "Date of Expiry"]
        label_width = 15
        entry_width = 31
        padding_y = 5
        padding_x = 1

        issue_date = datetime.date.today()
        twoWeeks = datetime.timedelta(weeks = 2)
        expirydate = issue_date + twoWeeks 
        
        regVar = StringVar()
        reg_label = Label(self.frame, text = issue_list[0]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 0, column = 0, pady = padding_y)
        reg_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = regVar)
        reg_entry.grid(row = 0, column = 1, pady = padding_y,  padx = padding_x, columnspan = 3)

        nameVar = StringVar()
        name_label = Label(self.frame, text = issue_list[1]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 1, column = 0, pady = padding_y)
        name_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = nameVar, state = 'disabled')
        name_entry.grid(row = 1, column = 1, pady = padding_y,  padx = padding_x, columnspan = 3)

        book1_label = Label(self.frame, text = "Book 1", font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 2, column = 1, pady = padding_y)
        book1_label = Label(self.frame, text = "Book 2", font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 2, column = 2, pady = padding_y)
        book1_label = Label(self.frame, text = "Book 3", font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 2, column = 3, pady = padding_y)

        bookid1Var = StringVar(value = 0)
        bookid2Var = StringVar(value = 0)
        bookid3Var = StringVar(value = 0)
        bookId_label = Label(self.frame, text = issue_list[2]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 3, column = 0, pady = padding_y)
        bookId1_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = bookid1Var)
        bookId1_entry.grid(row = 3, column = 1, pady = padding_y, padx = padding_x)
        bookId2_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = bookid2Var)
        bookId2_entry.grid(row = 3, column = 2, pady = padding_y, padx = padding_x)
        bookId3_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = bookid3Var)
        bookId3_entry.grid(row = 3, column = 3, pady = padding_y, padx = padding_x)
        
        title1Var = StringVar()
        title2Var = StringVar()
        title3Var = StringVar()
        bookId_title = Label(self.frame, text = issue_list[3]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 4, column = 0, pady = padding_y)
        title1_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = title1Var, state = 'disabled')
        title1_entry.grid(row = 4, column = 1, pady = padding_y, padx = padding_x)
        title2_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = title2Var, state = 'disabled')
        title2_entry.grid(row = 4, column = 2, pady = padding_y, padx = padding_x)
        title3_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = title3Var, state = 'disabled')
        title3_entry.grid(row = 4, column = 3, pady = padding_y, padx = padding_x)

        author1Var = StringVar()
        author2Var = StringVar()
        author3Var = StringVar()
        author_label = Label(self.frame, text = issue_list[4]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 5, column = 0, pady = padding_y)
        author1_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = author1Var, state = 'disabled')
        author1_entry.grid(row = 5, column = 1, pady = padding_y, padx = padding_x)
        author2_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = author2Var, state = 'disabled')
        author2_entry.grid(row = 5, column = 2, pady = padding_y, padx = padding_x)
        author3_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = author3Var, state = 'disabled')
        author3_entry.grid(row = 5, column = 3, pady = padding_y, padx = padding_x)

        isbn1Var = StringVar()
        isbn2Var = StringVar()
        isbn3Var = StringVar()
        bookId_isbn = Label(self.frame, text = issue_list[5]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 6, column = 0, pady = padding_y)
        isbn1_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = isbn1Var, state = 'disabled')
        isbn1_entry.grid(row = 6, column = 1, pady = padding_y, padx = padding_x)
        isbn2_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = isbn2Var, state = 'disabled')
        isbn2_entry.grid(row = 6, column = 2, pady = padding_y, padx = padding_x)
        isbn3_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = isbn3Var, state = 'disabled')
        isbn3_entry.grid(row = 6, column = 3, pady = padding_y, padx = padding_x)
        
        issueDateVar = StringVar(value = str(issue_date))
        issueDate_label = Label(self.frame, text = issue_list[6]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 7, column = 0, pady = padding_y)
        issueDate_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = issueDateVar, state = 'disabled')
        issueDate_entry.grid(row = 7, column = 1, pady = padding_y,  padx = padding_x, columnspan = 3)

        expiryDateVar = StringVar(value = str(expirydate))
        expirationDate_label = Label(self.frame, text = issue_list[7]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 8, column = 0, pady = padding_y)
        expirationDate_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = expiryDateVar, state = 'disabled')
        expirationDate_entry.grid(row = 8, column = 1, pady = padding_y, padx = padding_x, columnspan = 3)

        #button to submit
        submit_button = Button(self.frame, text = "Issue Book", width = 15, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.issue_book(self.frame, regVar.get(), nameVar.get(), bookid1Var.get(), title1Var.get(), author1Var.get(), isbn1Var.get(), bookid2Var.get(), title2Var.get(), author2Var.get(), isbn2Var.get(), bookid3Var.get(), title3Var.get(), author3Var.get(), isbn3Var.get(), issueDateVar.get(), expiryDateVar.get()))
        submit_button.grid(row = 9, column = 1, pady = padding_y, sticky = 'e')

        #button for autocompletion
        autofill_button = Button(self.frame, text = "Auto Fill", width = 15, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.autocomplete_issue(regVar.get(), bookid1Var.get(), bookid2Var.get(), bookid3Var.get(), nameVar, title1Var, title2Var, title3Var, author1Var, author2Var, author3Var, isbn1Var, isbn2Var, isbn3Var))
        autofill_button.grid(row = 9, column = 2, pady = padding_y, sticky = 'e')

        self.root.mainloop()

    def return_book(self):

        #create form
        issue_list = ["Register No", "Name", "Book Id", "Title", "Author", "ISBN", "Date of Issue", "Date of Expiry", "Date of Return", "Fine Calculated"]
        label_width = 15
        entry_width = 31
        padding_y = 5
        padding_x = 1
        
        return_date = datetime.date.today()

        regVar = StringVar()
        reg_label = Label(self.frame, text = issue_list[0]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 0, column = 0, pady = padding_y)
        reg_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = regVar)
        reg_entry.grid(row = 0, column = 1, pady = padding_y,  padx = padding_x, columnspan = 3)

        nameVar = StringVar()
        name_label = Label(self.frame, text = issue_list[1]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 1, column = 0, pady = padding_y)
        name_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = nameVar, state = 'disabled')
        name_entry.grid(row = 1, column = 1, pady = padding_y,  padx = padding_x, columnspan = 3)

        book1_label = Label(self.frame, text = "Book 1", font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 2, column = 1, pady = padding_y)
        book1_label = Label(self.frame, text = "Book 2", font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 2, column = 2, pady = padding_y)
        book1_label = Label(self.frame, text = "Book 3", font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 2, column = 3, pady = padding_y)

        bookid1Var = StringVar()
        bookid2Var = StringVar()
        bookid3Var = StringVar()
        bookId_label = Label(self.frame, text = issue_list[2]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 3, column = 0, pady = padding_y)
        bookId1_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = bookid1Var, state = 'disabled')
        bookId1_entry.grid(row = 3, column = 1, pady = padding_y, padx = padding_x)
        bookId2_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = bookid2Var, state = 'disabled')
        bookId2_entry.grid(row = 3, column = 2, pady = padding_y, padx = padding_x)
        bookId3_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = bookid3Var, state = 'disabled')
        bookId3_entry.grid(row = 3, column = 3, pady = padding_y, padx = padding_x)
        
        title1Var = StringVar()
        title2Var = StringVar()
        title3Var = StringVar()
        bookId_title = Label(self.frame, text = issue_list[3]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 4, column = 0, pady = padding_y)
        title1_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = title1Var, state = 'disabled')
        title1_entry.grid(row = 4, column = 1, pady = padding_y, padx = padding_x)
        title2_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = title2Var, state = 'disabled')
        title2_entry.grid(row = 4, column = 2, pady = padding_y, padx = padding_x)
        title3_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = title3Var, state = 'disabled')
        title3_entry.grid(row = 4, column = 3, pady = padding_y, padx = padding_x)

        author1Var= StringVar()
        author2Var= StringVar()
        author3Var= StringVar()
        author_label = Label(self.frame, text = issue_list[4]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 5, column = 0, pady = padding_y)
        author1_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = author1Var, state = 'disabled')
        author1_entry.grid(row = 5, column = 1, pady = padding_y, padx = padding_x)
        author2_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = author2Var, state = 'disabled')
        author2_entry.grid(row = 5, column = 2, pady = padding_y, padx = padding_x)
        author3_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = author3Var, state = 'disabled')
        author3_entry.grid(row = 5, column = 3, pady = padding_y, padx = padding_x)

        isbn1Var =StringVar()
        isbn2Var =StringVar()
        isbn3Var =StringVar()
        bookId_isbn = Label(self.frame, text = issue_list[5]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 6, column = 0, pady = padding_y)
        isbn1_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = isbn1Var, state = 'disabled')
        isbn1_entry.grid(row = 6, column = 1, pady = padding_y, padx = padding_x)
        isbn2_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = isbn2Var, state = 'disabled')
        isbn2_entry.grid(row = 6, column = 2, pady = padding_y, padx = padding_x)
        isbn3_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width-padding_x, textvariable = isbn3Var, state = 'disabled')
        isbn3_entry.grid(row = 6, column = 3, pady = padding_y, padx = padding_x)

        issueDateVar = StringVar()
        issueDate_label = Label(self.frame, text = issue_list[6]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 7, column = 0, pady = padding_y)
        issueDate_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = issueDateVar, state = 'disabled')
        issueDate_entry.grid(row = 7, column = 1, pady = padding_y,  padx = padding_x, columnspan = 3)

        expiryDateVar = StringVar()
        expirationDate_label = Label(self.frame, text = issue_list[7]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 8, column = 0, pady = padding_y)
        expirationDate_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = expiryDateVar, state = 'disabled')
        expirationDate_entry.grid(row = 8, column = 1, pady = padding_y, padx = padding_x, columnspan = 3)

        returnDateVar = StringVar(value = return_date)
        returnDate_label = Label(self.frame, text = issue_list[8]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 9, column = 0, pady = padding_y)
        returnDate_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = returnDateVar, state = 'disabled')
        returnDate_entry.grid(row = 9, column = 1, pady = padding_y,  padx = padding_x, columnspan = 3)

        fineVar = StringVar()
        fine_label = Label(self.frame, text = issue_list[9]+": ", anchor='e', font = ("arial", 13), width = label_width, pady = 1, bg = "#e3fdff").grid(row = 10, column = 0, pady = padding_y)
        fine_entry = ttk.Entry(self.frame, font = ("arial", 13), width = entry_width*3, textvariable = fineVar, state = 'disabled')
        fine_entry.grid(row = 10, column = 1, pady = padding_y, padx = padding_x, columnspan = 3)

        #button to submit
        submit_button = Button(self.frame, text = "Return Book", width = 15, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.return_book(self.frame, regVar.get(), returnDateVar.get(), fineVar.get(), bookid1Var.get(), bookid2Var.get(), bookid3Var.get()))
        submit_button.grid(row = 11, column = 1, pady = padding_y, sticky = 'e')

        #button for autocompletion
        autofill_button = Button(self.frame, text = "Auto Fill", width = 15, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.autocomplete_return(regVar.get(), nameVar, bookid1Var, bookid2Var, bookid3Var, title1Var, title2Var, title3Var, author1Var, author2Var, author3Var, isbn1Var, isbn2Var, isbn3Var, issueDateVar, expiryDateVar, return_date, fineVar))
        autofill_button.grid(row = 11, column = 2, pady = padding_y, sticky = 'e')

        self.root.mainloop()
    
    def book_fn(self):

        #search bar
        optionVar = StringVar()

        search_label = Label(self.frame, text = "Search By: ", font = ("Palatino", 15), bg = "#e3fdff")
        search_label.place(x = 125, y = 0-45) 

        search_combo = ttk.Combobox(self.frame, textvariable = optionVar, font = ("arial", 13), state = "readonly")
        search_combo["value"] = ("Show All", "title", "author", "bookId")
        search_combo.current(0)
        search_combo.place(x = 225, y = 0-45, width = 120)

        search_value = StringVar()
        search_entry = ttk.Entry(self.frame, textvariable = search_value, font = ("arial", 13), width = 50)
        search_entry.place(x = 355, y = 0-45)

        search_button = Button(self.frame, text = "Search", width = 10, bd=2, relief = 'raised', font = ("Palatino", 13), bg = "#40B7AD", fg="white", command = lambda:self.d.search_data("book", optionVar, search_value, self.data_preview))
        search_button.place(x = 825, y = 0-50)

        #dividing frames into 2 more frames
        form_frame = Frame(self.frame, bd=2, relief = 'ridge', bg = "#e3fdff", pady = 70)
        form_frame.place(x = 0, y = 0, width = 350, height = self.height-135)
        display_frame = Frame(self.frame, bd=2, relief = 'ridge', bg = "#e3fdff")
        display_frame.place(x = 350, y = 0, width = self.width-350, height = self.height-135)

        add_list = ["Book Id", "Title", "Author", "Publisher", "Genre", "Rack Id", "ISBN"] #set status to available initially
        
        #create form
        label_width = 15
        entry_width = 31
        padding_y = 5
        padding_x = 1

        #clear entries
        clearAll_button = Button(form_frame, text = "Clear All", width = 10, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.clearEntries(form_frame))
        clearAll_button.grid(row = 0, column = 2, pady = padding_y)

        #defining label and entries
        bookIdVar = StringVar()
        bookId_label = Label(form_frame, text = add_list[0]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 1, column = 0, pady = padding_y)
        bookId_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = bookIdVar).grid(row = 1, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        titleVar = StringVar()
        title_label = Label(form_frame, text = add_list[1]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 2, column = 0, pady = padding_y)
        title_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = titleVar).grid(row = 2, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        authorVar = StringVar()
        author_label = Label(form_frame, text = add_list[2]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 3, column = 0, pady = padding_y)
        author_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = authorVar).grid(row = 3, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        publisherVar = StringVar()
        publisher_label = Label(form_frame, text = add_list[3]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 4, column = 0, pady = padding_y)
        publisher_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = publisherVar).grid(row = 4, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        genreVar = StringVar()
        genre_label = Label(form_frame, text = add_list[4]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 5, column = 0, pady = padding_y)
        genre_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = genreVar).grid(row = 5, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        rackVar = StringVar()
        rackId = Label(form_frame, text = add_list[5]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 6, column = 0, pady = padding_y)
        rackId_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = rackVar).grid(row = 6, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        isbnVar = StringVar()
        isbn_label = Label(form_frame, text = add_list[6]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 7, column = 0, pady = padding_y)
        isbn_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = isbnVar).grid(row = 7, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)
        
        var_list = [bookIdVar, titleVar, authorVar, publisherVar, genreVar, rackVar, isbnVar]

        #button to add
        add_button = Button(form_frame, text = "Add", width = 10, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.insert_book(form_frame, self.data_preview, bookIdVar.get(), titleVar.get(), authorVar.get(), publisherVar.get(), rackVar.get(), genreVar.get(), isbnVar.get(), state1="available"))
        add_button.grid(row = 8, column = 0, pady = 15, sticky = 'e')

        #button to delete
        delete_button = Button(form_frame, text = "Delete", width = 10, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.delete_data("book", "bookId", bookIdVar, self.data_preview))
        delete_button.grid(row = 8, column = 1, pady = 15, sticky = 'e')

        #button to update
        update_button = Button(form_frame, text = "Update", width = 10, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.update_book(var_list, self.data_preview))
        update_button.grid(row = 8, column = 2, pady = 15, sticky = 'e')

        #display data headers
        self.display_data(display_frame, headers=("Book Id", "Title", "Author", "Publisher", "Rack Id", "Genre", "ISBN", "Status"))

        #select row and set entry values
        self.data_preview.bind("<ButtonRelease-1>", lambda a:self.d.get_cursor('' ,self.data_preview, var_list))

        #show data preview
        self.d.fetch_data(table='book', preview_table=self.data_preview)

        self.root.mainloop()
    
    def member_fn(self):
        #search bar
        optionVar = StringVar()

        search_label = Label(self.frame, text = "Search By: ", font = ("Palatino", 15), bg = "#e3fdff")
        search_label.place(x = 125, y = 0-45) 

        search_combo = ttk.Combobox(self.frame, textvariable = optionVar, font = ("arial", 13), state = "readonly")
        search_combo["value"] = ("Show All", "name", "reg_num")
        search_combo.current(0)
        search_combo.place(x = 225, y = 0-45, width = 120)

        search_value = StringVar()
        search_entry = ttk.Entry(self.frame, font = ("arial", 13), width = 50, textvariable = search_value)
        search_entry.place(x = 355, y = 0-45)

        search_button = Button(self.frame, text = "Search", width = 10, bd=2, relief = 'raised', font = ("Palatino", 13), bg = "#40B7AD", fg="white", command = lambda:self.d.search_data("member", optionVar, search_value, self.data_preview))
        search_button.place(x = 825, y = 0-50)

        #dividing frames into 2 more frames
        form_frame = Frame(self.frame, bd=2, relief = 'ridge', bg = "#e3fdff", pady = 70)
        form_frame.place(x = 0, y = 0, width = 350, height = self.height-135)
        display_frame = Frame(self.frame, bd=2, relief = 'ridge', bg = "#e3fdff")
        display_frame.place(x = 350, y = 0, width = self.width-350, height = self.height-135)

        add_list = ["Name", "Register No", "Mobile", "Email", "Address"] #set status to available initially
        
        #create form
        label_width = 15
        entry_width = 31
        padding_y = 5
        padding_x = 1

        #to clear all entries
        clearAll_button = Button(form_frame, text = "Clear All", width = 10, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.clearEntries(form_frame))
        clearAll_button.grid(row = 0, column = 2, pady = padding_y)
        
        #defining labels and entries
        nameVar = StringVar()
        name_label = Label(form_frame, text = add_list[0]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 1, column = 0, pady = padding_y)
        name_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = nameVar).grid(row = 1, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        regVar = StringVar()
        reg_label = Label(form_frame, text = add_list[1]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 2, column = 0, pady = padding_y)
        reg_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = regVar).grid(row = 2, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        mobileVar = StringVar()
        mobile_label = Label(form_frame, text = add_list[2]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 3, column = 0, pady = padding_y)
        mobile_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = mobileVar).grid(row = 3, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        emailVar = StringVar()
        email_label = Label(form_frame, text = add_list[3]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 4, column = 0, pady = padding_y)
        email_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = emailVar).grid(row = 4, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)

        addressVar = StringVar()
        address_label = Label(form_frame, text = add_list[4]+": ", width = label_width, anchor='e', font = ("arial", 13), pady = 1, bg = "#e3fdff").grid(row = 5, column = 0, pady = padding_y)
        address_entry = ttk.Entry(form_frame, font = ("arial", 13), textvariable = addressVar).grid(row = 5, column = 1, pady = padding_y, padx = padding_x, columnspan = 2)
        
        var_list = [nameVar, regVar, mobileVar, emailVar, addressVar]

        #button to add
        add_button = Button(form_frame, text = "Add", width = 12, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.insert_member(form_frame, self.data_preview, nameVar.get(), regVar.get(), mobileVar.get(), emailVar.get(), addressVar.get()))
        add_button.grid(row = 6, column = 0, padx = 5, pady = 15, sticky = 'e')

        #button to delete
        delete_button = Button(form_frame, text = "Delete", width = 12, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.delete_data("member", "reg_num", regVar, self.data_preview))
        delete_button.grid(row = 6, column = 1, padx = 5, pady = 15)

        #button to update
        update_button = Button(form_frame, text = "Update", width = 12, bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.update_member(var_list, self.data_preview))
        update_button.grid(row = 6, column = 2, padx = 5, pady = 15)

        #display data headings
        self.display_data(display_frame, headers=("Name", "Register No", "Mobile", "Email", "Address"))

        #select row and set entry values
        self.data_preview.bind("<ButtonRelease-1>", lambda a:self.d.get_cursor('', self.data_preview, var_list))

        #preview data
        self.d.fetch_data(table='member', preview_table=self.data_preview)

        self.root.mainloop()
    
    def reports(self):
        
        today = datetime.date.today()

        #start date
        dateiVar = StringVar()
        
        #end date
        datefVar = StringVar()

        #frame for displaying preview
        preview_frame = Frame(self.frame, bg = "#e3fdff", relief = 'ridge', bd = 2)
        preview_frame.place(x = 0, y = 35, width = self.width, height = self.height-170)

        #searching
        start_date_label = Label(self.frame, text = "Start Date: ", bg = "#e3fdff", anchor = 'e')
        start_date_label.grid(row = 0, column = 0, padx = 10, sticky = 'e')

        startDate = DateEntry(self.frame, width=12, year=int(today.strftime("%Y")), month=int(today.strftime("%m")), day=int(today.strftime("%d")), background='darkblue', foreground='white', textvariable = dateiVar)
        startDate.grid(row = 0, column = 1, padx = 10, sticky = 'w')
        
        end_date_label = Label(self.frame, text = "End Date: ", bg = "#e3fdff", anchor = 'e')
        end_date_label.grid(row = 0, column = 2, padx = 10, sticky = 'e')

        endDate = DateEntry(self.frame, width=12, year=int(today.strftime("%Y")), month=int(today.strftime("%m")), day=int(today.strftime("%d")), background='darkblue', foreground='white', textvariable = datefVar)
        
        endDate.grid(row = 0, column = 3, padx = 10, sticky = 'w')

        search_button = Button(self.frame, text = "Search", bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.time_report(self.data_preview, str(startDate.get_date()), str(endDate.get_date())))
        search_button.grid(row = 0, column = 4, padx = 10)

        searchAll_button = Button(self.frame, text = "Search All", bd=2, relief = 'raised', font = ("Palatino", 10, "bold"), bg = "#40B7AD", fg="white", command = lambda:self.d.fetch_data(table='report', preview_table=self.data_preview))
        searchAll_button.grid(row = 0, column = 5, padx = 10)

        #display data headings
        self.display_data(preview_frame, headers=("Reg no.", "Name", "Book Id 1", "Title 1", "Author 1", "ISBN 1", "Book Id 2", "Title 2", "Author 2", "ISBN 2", "Book Id 3", "Title 3", "Author 3", "ISBN 3", "Issue Date", "Expiry Date", "Return Date", "Fine"))

        #preview data
        self.d.fetch_data(table='report', preview_table=self.data_preview)

        self.root.mainloop()
