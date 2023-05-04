# Importing standard modules
from tkinter import*
from datetime import datetime
# import time
import os
from tkinter import messagebox

#Can I pull this out of function?
#def directory():
"""Defining directory location where journal entries will be saved"""
path = "C:\\Users\\skyle\\OneDrive\\Documents\\DMACC\\CIS 189\\Final Project\\Journal Entries"
os.chdir(path)
#directory()



class window(Frame):
    '''This class contains the widgets that will allow user to write into files'''
    def __init__(self,master=None):
        #intialization of the frame
        Frame.__init__(self,master)
        self.master=master
        self.master.title("Diary")
        title=Label(self.master,text="Title").pack()

        #Entry box to get title of the file from the user.
        self.title_box=Entry(self.master)
        self.title_box.pack()

        scrollbar=Scrollbar(self.master).pack(side=RIGHT,fill=Y)#scrollbar
        Label(self.master,text="Content").pack()

        #Text for the user to write his thoughts
        self.content_box=Text(self.master)
        self.content_box.pack()

        #This button is binded to the function "save_file" wich saves the file in the specified path'''
        save_button=Button(self.master,text="Save",width=10,command=self.save_file).pack()

    def save_file(self):
        """This function saves the content written by the user as a text file"""

        current_date_and_time = datetime.now()
        date = current_date_and_time.strftime("%d")
        # Opportunity for dictionary to switch this to month or number of month
        month = current_date_and_time.strftime("%B")
        year = current_date_and_time.strftime("%Y")
        file_name = self.title_box.get()+" "+date+month+year+".txt"
        f = open(file_name, "w+")
        f.write(self.content_box.get("1.0", END))
        messagebox.showinfo("Entry saved", "Journal entry saved successfully! ")