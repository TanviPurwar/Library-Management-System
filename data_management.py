from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import re

class Data:
    
    def __init__(self, frame):
        print(self)

        self.frame = frame

        self.lms_db_connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "mySQL@123",
            database = 'lms_db'
        )
    
    def clearEntries(self, frame):

        temp = ttk.Entry(frame, font = ("arial", 13), width = 3)

        for widget in frame.winfo_children():
            if type(widget) == type(temp):
                widget.delete(0, "end")

    def fetch_data(self, table, preview_table):
        
        self.mycursor = self.lms_db_connection.cursor()
        self.mycursor.execute("SELECT * FROM {}".format(table))
        rows = self.mycursor.fetchall()

        #delete data from table and fill again
        if len(rows) != 0:
            preview_table.delete(*preview_table.get_children())
            for i in rows:
                preview_table.insert("", 'end', values = i)

            self.lms_db_connection.commit()
    
    def time_report(self, preview_table, start_date, end_date):

        self.mycursor = self.lms_db_connection.cursor()
        self.mycursor.execute("SELECT * FROM report")
        rows = self.mycursor.fetchall()

        #delete data from table and fill again
        if len(rows) != 0:
            preview_table.delete(*preview_table.get_children())
            for i in rows:
                if i[13] >= start_date and i[13] <= end_date:
                    preview_table.insert("", 'end', values = i)

            self.lms_db_connection.commit()


    def get_cursor(self, events="", preview_table='', var_list=[]):
        
        cursor_row = preview_table.focus()
        content = preview_table.item(cursor_row)
        row_values = content["values"]

        for i in range(0, len(var_list)):
            var_list[i].set(row_values[i])
    
    def autocomplete(self, column_name, table, primary_key, foreign_key_value, entryVal):
        
        try:
            self.mycursor = self.lms_db_connection.cursor()
            #query = "SELECT " + column_name + " FROM " + ref_table + " WHERE " + table + "." + foreign_key + "=" + ref_table + "." + primary_key
            query = "SELECT " + column_name + " FROM " + table + " WHERE " + primary_key + " = %s"
            value = (foreign_key_value,)
            
            self.mycursor.execute(query, value)
            res = str(self.mycursor.fetchone())
            entryVal.set(res[2:len(res)-3])
            

        except Exception as es:
            messagebox.showerror("Error", "Error: {}".format(es), parent = self.frame)

    def insert_book(self, frame, preview_table, bookid1, title1, author1, publisher1, shelfid1, genre1, isbn1, state1):
        
        if title1=='' or bookid1=='' or author1=='' or publisher1=='' or shelfid1=='' or genre1=='' or isbn1=='':
            messagebox.showerror("Error", "All entries need to be filled")
        
        else:
            try:

                self.mycursor = self.lms_db_connection.cursor()
                query = """INSERT INTO book (bookId, title, author, publisher, shelf_id, genre, isbn, state) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                
                val = (bookid1, title1, author1, publisher1, shelfid1, genre1, isbn1, state1)
                self.mycursor.execute(query, val)
                self.lms_db_connection.commit()

                self.fetch_data(table='book', preview_table = preview_table)

                self.mycursor.close()

                messagebox.showinfo("Success", "Book added successfully")
                self.clearEntries(frame)

            except Exception as es:
                messagebox.showerror("Error", "Error: {}".format(es), parent = self.frame)
        
    
    def insert_member(self, frame, preview_table, name1, reg1, mobile1, email1, address1):
        
        if name1=='' or reg1=='' or mobile1=='' or email1=='' or address1=='':
            messagebox.showerror("Error", "All entries need to be filled")
        else:
            try:
                self.mycursor = self.lms_db_connection.cursor()

                insert_query = """INSERT INTO member (name, reg_num, mobile, email, address) 
                                VALUES (%s, %s, %s, %s, %s)"""
                
                val = (name1, reg1, mobile1, email1, address1)
                self.mycursor.execute(insert_query, val)
                self.lms_db_connection.commit()

                self.fetch_data(table='member', preview_table = preview_table)

                self.mycursor.close()

                messagebox.showinfo("Success", "Member added successfully")
                self.clearEntries(frame)

            except Exception as es:
                messagebox.showerror("Error", "Error: {}".format(es))
    
    def update_book(self, var_list, preview_table):

        try:
            self.mycursor = self.lms_db_connection.cursor()
            self.mycursor.execute('''
                UPDATE book
                SET title = %s, author = %s, publisher = %s, genre = %s, shelf_id = %s, isbn = %s
                WHERE bookId = %s
            ''', (var_list[1].get(), var_list[2].get(), var_list[3].get(), var_list[4].get(), int(var_list[5].get()), var_list[6].get(), var_list[0].get()))

            self.lms_db_connection.commit()

            self.fetch_data(table='book', preview_table = preview_table)

            self.mycursor.close()

            messagebox.showinfo("Success", "Book updated successfully")

        except Exception as es:
            messagebox.showerror("Error", "Error: {}".format(es), parent = self.frame)
        
    def update_member(self, var_list, preview_table):

        try:
            self.mycursor = self.lms_db_connection.cursor()
            self.mycursor.execute('''
                UPDATE member
                SET name = %s, mobile = %s, email = %s, address = %s
                WHERE reg_num = %s
            ''', (var_list[0].get(), var_list[2].get(), var_list[3].get(), var_list[4].get(), var_list[1].get(),))

            self.lms_db_connection.commit()

            self.fetch_data(table='member', preview_table = preview_table)

            self.mycursor.close()

            messagebox.showinfo("Success", "Member updated successfully")

        except Exception as es:
            messagebox.showerror("Error", "Error: {}".format(es), parent = self.frame)

    def delete_data(self, table, reference, reference_value, preview_table):

        if messagebox.askyesno("Delete " + table, " Do you want to delete " + table + " ?"):
            
            try:
                self.mycursor = self.lms_db_connection.cursor()
                
                query = "DELETE FROM " + table + " WHERE " + reference + " = %s"
                value = (reference_value.get(),)
                self.mycursor.execute(query, value)

                self.lms_db_connection.commit()

                self.fetch_data(table, preview_table)

                self.mycursor.close()

                messagebox.showinfo("Success", table + " deleted successfully")

            except Exception as es:
                messagebox.showerror("Error", "Error: {}".format(es))
    
    def search_data(self, table, search_option, search_value, preview_table):

        try:
            self.mycursor = self.lms_db_connection.cursor()

            if search_option.get() == 'Show All':
                self.fetch_data(table, preview_table)
            
            else:
                self.mycursor.execute('SELECT * FROM ' + table + ' WHERE ' + str(search_option.get()) + " LIKE '%" + str(search_value.get()) + "%'")

                rows_value = self.mycursor.fetchall()
                if len(rows_value) != 0:
                    preview_table.delete(*preview_table.get_children())

                    for i in rows_value:
                        preview_table.insert("", 'end', values = i)
                        self.lms_db_connection.commit()
                
                #self.lms_db_connection.close()
        
        except Exception as es:
            messagebox.showerror("Error", "Error: {}".format(es))
    
    def issue_book(self, frame, reg_num1, name1, bookid1, title1, author1, isbn1, bookid2, title2, author2, isbn2, bookid3, title3, author3, isbn3, issuedate, expirydate):


        try:

            self.mycursor = self.lms_db_connection.cursor()

            #to check if member has pending records
            query0 = '''SELECT *
                    FROM report
                    WHERE reg_num = %s AND returnDate = %s
            '''
            value0 = (reg_num1, '0000-00-00',)
            self.mycursor.execute(query0, value0)
            
            row = self.mycursor.fetchone()
            print(row)

            if row is not None:
                messagebox.showerror("Error", "Error: Member has pending returns")
                return

            query = """INSERT INTO report(reg_num, name, bookId1, title1, author1, isbn1, bookId2, title2, author2, isbn2, bookId3, title3, author3, isbn3, issueDate, expiryDate, returnDate, fine) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = (reg_num1, name1, bookid1, title1, author1, isbn1, bookid2, title2, author2, isbn2, bookid3, title3, author3, isbn3, issuedate, expirydate, '0000-00-00', '0')
            self.mycursor.execute(query, val)
            self.lms_db_connection.commit()

            #update status to unavailable
            query1 = '''UPDATE book
                        SET state = %s
                        where bookId = %s
            '''
            value1 = ('unavailable', bookid1,)
            self.mycursor.execute(query1, value1)
            self.lms_db_connection.commit()

            query2 = '''UPDATE book
                        SET state = %s
                        where bookId = %s
            '''
            value2 = ('unavailable', bookid2,)
            self.mycursor.execute(query2, value2)
            self.lms_db_connection.commit()

            query3 = '''UPDATE book
                        SET state = %s
                        where bookId = %s
            '''
            value3 = ('unavailable', bookid3,)
            self.mycursor.execute(query3, value3)
            self.lms_db_connection.commit()

            #close connection
            self.lms_db_connection.commit()

            self.mycursor.close()

            messagebox.showinfo("Success", "Book issued successfully")

            self.clearEntries(frame)

        except Exception as es:
            messagebox.showerror("Error", "Error: {}".format(es))
    
    def return_book(self, frame, regVar, return_date, fineVar, bookid1Var, bookid2Var, bookid3Var):

            try:

                self.mycursor = self.lms_db_connection.cursor()

                query = '''
                        UPDATE report
                        SET returnDate = %s, fine = %s
                '''
                value = (return_date, fineVar,)
                self.mycursor.execute(query, value)
                self.lms_db_connection.commit()

                print(self.mycursor.fetchone())

                #update status to available
                query1 = '''UPDATE book
                            SET state = %s
                            where bookId = %s
                '''
                value1 = ('available', bookid1Var,)
                self.mycursor.execute(query1, value1)
                self.lms_db_connection.commit()

                query2 = '''UPDATE book
                            SET state = %s
                            where bookId = %s
                '''
                value2 = ('available', bookid2Var,)
                self.mycursor.execute(query2, value2)
                self.lms_db_connection.commit()

                query3 = '''UPDATE book
                            SET state = %s
                            where bookId = %s
                '''
                value3 = ('available', bookid3Var,)
                self.mycursor.execute(query3, value3)
                self.lms_db_connection.commit()
                
                self.lms_db_connection.close()

                messagebox.showinfo("Success", "Book returned successfully")
                self.clearEntries(frame)

            except Exception as es:
                messagebox.showerror("Error", "Error: {}".format(es))            

    
    def autocomplete_issue(self, regno, bookId1, bookId2, bookId3, nameVar, title1Var, title2Var, title3Var, author1Var, author2Var, author3Var, isbn1Var, isbn2Var, isbn3Var):

        self.autocomplete('name', 'member', 'reg_num', regno, nameVar)

        self.autocomplete('title', 'book', 'bookId', bookId1, title1Var)
        self.autocomplete('title', 'book', 'bookId', bookId2, title2Var)
        self.autocomplete('title', 'book', 'bookId', bookId3, title3Var)

        self.autocomplete('author', 'book', 'bookId', bookId1, author1Var)
        self.autocomplete('author', 'book', 'bookId', bookId2, author2Var)
        self.autocomplete('author', 'book', 'bookId', bookId3, author3Var)

        self.autocomplete('isbn', 'book', 'bookId', bookId1, isbn1Var)
        self.autocomplete('isbn', 'book', 'bookId', bookId2, isbn2Var)
        self.autocomplete('isbn', 'book', 'bookId', bookId3, isbn3Var)
        
    def autocomplete_return(self, regno, nameVar, bookId1Var, bookId2Var, bookId3Var, title1Var, title2Var, title3Var, author1Var, author2Var, author3Var, isbn1Var, isbn2Var, isbn3Var, issueDateVar, expiryDateVar, returnDate_val, fineVar):

        try:
            self.mycursor = self.lms_db_connection.cursor()

            query = '''SELECT *
                    FROM report
                    WHERE reg_num = %s AND returnDate = %s
            '''
            value = (regno, '0000-00-00',)
            self.mycursor.execute(query, value)
            
            row = self.mycursor.fetchone()
            print(row)

            if row is None:
                messagebox.showerror("Error", "Error: Member has no pending returns")
                return
            
            self.autocomplete('name', 'member', 'reg_num', regno, nameVar)
            
            #fetch book ids in record
            bookid1 = row[2]
            bookid2 = row[6]
            bookid3 = row[10]

            issueDate = row[14]
            expiryDate = row[15]

            #autocomplete rest columns
            bookId1Var.set(bookid1)
            bookId2Var.set(bookid2)
            bookId3Var.set(bookid3)

            self.autocomplete('title', 'book', 'bookId', bookid1, title1Var)
            self.autocomplete('title', 'book', 'bookId', bookid2, title2Var)
            self.autocomplete('title', 'book', 'bookId', bookid3, title3Var)

            self.autocomplete('author', 'book', 'bookId', bookid1, author1Var)
            self.autocomplete('author', 'book', 'bookId', bookid2, author2Var)
            self.autocomplete('author', 'book', 'bookId', bookid3, author3Var)

            self.autocomplete('isbn', 'book', 'bookId', bookid1, isbn1Var)
            self.autocomplete('isbn', 'book', 'bookId', bookid2, isbn2Var)
            self.autocomplete('isbn', 'book', 'bookId', bookid3, isbn3Var)

            issueDateVar.set(issueDate)
            expiryDateVar.set(expiryDate)

            #calculate fine
            pending_days = returnDate_val - expiryDate
            d = pending_days.days
            if d > 0:
                fineVar.set(str(d*5))
            else:
                fineVar.set(0)
        
        except Exception as es:
            messagebox.showerror("Error", "Error: {}".format(es)) 