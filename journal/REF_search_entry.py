"""This will contain a class and frame widgets that allow the user to either search by date or keyword, and will return a list of journal entries that meet the criteria."""

# Imports?
from tkinter import*

# Class SearchWindow
class SearchWindow(Frame):

    def __init__(self, master=None):
        # Setting up Search Window frame
        Frame.__init__(self, master)
        self.master.title("Diary")
        self.master.geometry("400x300")