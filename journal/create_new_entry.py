# Importing standard modules
from tkinter import*
from datetime import datetime
# import time
import os
from tkinter import messagebox

# Can I pull this out of function?
# def directory():
"""Defining directory location where journal entries will be saved"""
path = "C:\\Users\\skyle\\OneDrive\\Documents\\DMACC\\CIS 189\\Final Project\\Journal Entries"
os.chdir(path)
# directory()


class NewEntryWindow(Frame):
    """This class contains the widgets that will allow user to write into files"""
    def __init__(self, master=None):
        # Setting up Create New Entry Window frame
        Frame.__init__(self, master)
        self.master=master
        self.master.title("Create New Entry")
        Label(self.master, text="Title").pack()

        # Entry box to get journal entry title
        self.title_box = Entry(self.master)
        self.title_box.pack()

        # scrollbar
        Scrollbar(self.master).pack(side=RIGHT,fill=Y)
        Label(self.master, text="Content").pack()

        # Text box where journal entry is typed
        self.content_box = Text(self.master)
        self.content_box.pack()

        # Save button is linked to the function "save_file" which saves the file in the specified path'''
        Button(self.master, text="Save", width=10, command=self.save_file).pack()

    def save_file(self):
        """This function saves the content written by the user as a text file and creates a file title name using title entry and current date"""

        current_date_and_time = datetime.now()
        date = current_date_and_time.strftime("%d")
        # Opportunity for dictionary to switch this to month or number of month
        month = current_date_and_time.strftime("%B")
        year = current_date_and_time.strftime("%Y")

        # Input validation that Title and Content contain characters
        try:
            if len(self.title_box.get()) > 0 and len(self.content_box.get("1.0", END)) > 0:
                file_name = self.title_box.get()+" "+date+month+year+".txt"
                f = open(file_name, "w+")
                f.write(self.content_box.get("1.0", END))
                messagebox.showinfo("Entry saved", "Journal entry saved successfully! ")
            else:
                raise ValueError
        except:
            messagebox.showinfo("MISSING TITLE AND/OR CONTENT", "No characters detected in Title and/or Content fields")


