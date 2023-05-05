#Modules imported
from tkinter import*
import os
from tkinter import messagebox


class EditWindow(Frame):
    """This class has the UI and functions to edit a file stored previously"""

    def __init__(self, master=None):
        # Setting up Edit Entry Window frame
        Frame.__init__(self, master)
        self.master.title("Diary")
        self.master.geometry("400x300")

        # Diplaying the files in the path for the user to select.
        Label(self.master, text="Select a file").pack()
        path = "C:\\Users\\skyle\\OneDrive\\Documents\\DMACC\\CIS 189\\Final Project\\Journal Entries"
        self.file_names = os.listdir(path)
        self.srch_box = Entry(self.master)
        self.srch_box.pack()
        file_list = Listbox(self.master)
        file_list.pack()
        for i in range(0, len(self.file_names)):
            file_list.insert(END, self.file_names[i])

        # Edit button linked to edit_entry function which allows user to edit the selected file.
        Button(self.master, text="Edit File", width=20, command=self.edit_entry).pack()


    def edit_entry(self):
        """This function attempts to open the file name typed in by user.
        If it cannot find requested file, shows error message box"""
        self.file_name = self.srch_box.get()
        if self.file_name in self.file_names:
            f = open(self.file_name, "r")
            content = f.read()
            edit_window = Tk()
            t = Text(edit_window)
            t.pack()
            edit_window.title(self.file_name)
            t.insert("end", content)

            # Inner function to save edited file.
            def save_file():
                g = open(self.file_name, "w+")
                g.write(t.get("1.0", END))
                messagebox.showinfo("MyJournal", "Your entry edits have been saved successfully")
            Button(edit_window, text="Save", command=save_file).pack()
        else:
            messagebox.showinfo("MyJournal", "File doesn't exist")
