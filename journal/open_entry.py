#modules imported
from tkinter import*
import os
from tkinter import messagebox


class ReadWindow(Frame):
    """This class has the UI and functions to read a file stored previously"""
    def __init__(self, master=None):
        # Setting up Open Entry Window frame
        Frame.__init__(self, master)
        self.master = master
        self.master.title("View Entries")
        self.master.geometry("400x300")

        # Display all the files present in the directory
        Label(self.master,text="Select a file").pack(side=TOP)
        path = "C:\\Users\\skyle\\OneDrive\\Documents\\DMACC\\CIS 189\\Final Project\\Journal Entries"
        self.file_names = os.listdir(path)
        self.srch_box = Entry(self.master)
        self.srch_box.pack()
        file_list = Listbox(self.master)
        file_list.pack()
        for i in range(0, len(self.file_names)):
            file_list.insert(END, self.file_names[i])

        """def file_selected(event):
            # get selected indices
            selected_entry = file_list.curselection()

        file_list.bind('<<ListboxSelect>>', file_selected)"""

        # Read button is linked the function "read_file" which displays the content in the file.
        Button(self.master, text="Read", width=20, command=self.read_file).pack(side=BOTTOM)

    def read_file(self):
        self.file_name = self.srch_box.get()

        """If the specified file is present it is displayed in a text
         for the user to read. Else an error is displayed"""
        try:
            assert self.file_name in self.file_names
            f = open(self.file_name, "r")
            contents = f.read()
            read_window = Tk()
            read_window.title(self.file_name)
            t = Text(read_window)
            t.pack()
            t.insert("end", contents)
            t.config(state=DISABLED)
            read_window.mainloop()
        except:
            messagebox.showinfo("MyJournal", "File doesn't exist")
