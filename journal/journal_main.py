"""This contains the main journal app that will import """

# Importing modules
from tkinter import*
from tkinter import messagebox

import create_new_entry
import open_entry
import search_entry
import edit_entry


class LoginInterface(Frame):
    """his class contains the login section of the app.The user have
    to enter a password to access the main application."""
    def __init__(self, master=None, pwrd=None):
        # Initiating the login frame
        Frame.__init__(self, master)
        self.master = master
        self.security()

    # function that holds the widgets of login window
    def security(self):
        self.master.title("LOGIN")
        self.pack(fill=BOTH, expand=1)
        Label(self, text="PASSWORD").grid(column=0, row=0)

        # Entry to get a password input from the user
        self.pwrd = Entry(self)
        self.pwrd.focus_set()
        self.pwrd.grid(column=1, row=0)

        # login button linked to log in function
        login = Button(self, text="login", width=20, command=self.login)
        login.grid(column=1, row=2)

    def login(self):
        """this function is initiated by the "login" Button. It checks if the
        password given by the user is correct"""

        # Input validation to ensure a password is entered
        try:
            if len(self.pwrd.get()) > 0:
                # if the password given is correct the following get executed
                if self.pwrd.get() == "123":
                    # destroys the present login window
                    a.destroy()

                    # initiates the main application
                    b = Tk()
                    b.geometry("500x700")
                    # 500 x 500 with only 3 buttons
                    app_b = Journal(b)
                    app_b.mainloop()  # mainloop for the program will run until close

                # else statement on handling wrong password
                else:
                    messagebox.showinfo("ERROR ", "Incorrect password, please try again!")
            else:
                raise ValueError

        except:
            messagebox.showinfo("ERROR - NO ENTRY", "No password entered, please try again!")


class Journal(Frame):
    """The journal class contains the main UI and application.
    Main application contains five buttons: Write, Read, Search, Edit, and Exit"""

    # Initiating main UI window frame
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.master.title("MyJournal")
        self.pack(fill=BOTH, expand=1)

        # Write button linked to Write function.
        write_button = Button(self, text="Write", width=100, height=10, command=self.write)
        write_button.pack()

        # Read button linked to Read function.
        read_button = Button(self, text="Read", width=100, height=10, command=self.read)
        read_button.pack()

        # Search button linked to Search function.
        search_button = Button(self, text="Search", width=100, height=10, command=self.search)
        search_button.pack()

        # Edit button linked to Edit function.
        edit_button = Button(self, text="Edit", width=100, height=10, command=self.edit)
        edit_button.pack()

        # The Main window Exit/destroy function. Currently, just clears window rather than closing it.
        exit_button = Button(self, text='Exit', width=100, height=5, command=self.destroy)
        exit_button.pack()


    def write(self):
        """This function call to the create_new_entry module (and opens the corresponding window)"""
        b = create_new_entry.NewEntryWindow(a)
        b.mainloop()

    def read(self):
        """This function call to the open_entry module (and opens the corresponding window)"""
        b = open_entry.ReadWindow(a)
        b.mainloop()

    def search(self):
        """This function calls to the search_entry module (and opens the corresponding window)"""
        b = search_entry.SearchWindow(a)
        b.mainloop()

    def edit(self):
        """This function call to the edit_entry module (and opens the corresponding window)"""
        b = edit_entry.EditWindow(a)
        b.mainloop()


"""Creating the instance of the login class and running the program"""
a = Tk()
a.geometry("250x50")
app = LoginInterface(a)
app.mainloop()
