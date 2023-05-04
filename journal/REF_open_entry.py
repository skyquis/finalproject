#modules imported
from tkinter import*
import os
from tkinter import messagebox
import time


class window(Frame):
    """This class contains the widgets that allows the user to read the files stored previously"""
    def __init__(self, master=None):
        #intilization of the frame
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary")
        self.master.geometry("400x300")

        #Display all the files present in the directory
        Label(self.master,text="Select a file").pack(side=TOP)
        path="C:\\Users\\skyle\\OneDrive\\Documents\\DMACC\\CIS 189\\Final Project\\Journal Entries"
        self.file_names=os.listdir(path)
        self.srch_box=Entry(self.master)
        self.srch_box.pack()
        file_list=Listbox(self.master)
        file_list.pack()
        for i in range(0,len(self.file_names)):
            file_list.insert(END, self.file_names[i])

        def file_selected(event):
            # get selected indices
            selected_entry = file_list.curselection()

        file_list.bind('<<ListboxSelect>>', file_selected)


        #Read button binded to the function "read_file" which displays the content in the file.
        read_button=Button(self.master,text="Read",width=20,command=self.read_file(file_list.curselection()).pack(side=BOTTOM))




    def read_file(self, selected_entry):
        self.selected_entry = selected_entry
        print("selected entry", self.selected_entry)
        print("all file names", self.file_names)

        '''If the specified file is present it is displayed in a text
         for the user to read.If the specified file is not present it 
         displays an error'''
        if self.selected_entry in self.file_names:
            f=open(self.file_name,"r")
            contents=f.read()
            read_window=Tk()
            read_window.title(self.file_name)
            t=Text(read_window)
            t.pack()
            t.insert("end",contents)
            t.config(state=DISABLED)
            read_window.mainloop()
        else:
            messagebox.showinfo("Diary","File doesn't exist")
