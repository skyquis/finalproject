"""This will contain a class and frame widgets that allow the user to either search by date or keyword, and will return a list of journal entries that meet the criteria."""

# Imports?
from tkinter import*
import os

# Class SearchWindow
class SearchWindow(Frame):

    def __init__(self, master=None):
        # Setting up Search Window frame
        Frame.__init__(self, master)
        self.master.title("Search for entry")
        self.master.geometry("400x300")
        # Starting with keyword search label, entry box, and button
        # Keyword search label
        Label(self.master, text="Keyword Search").pack()

        # Entry box to get keyword search value
        self.title_box = Entry(self.master)
        self.title_box.pack()

        # Keyword search criteria label
        Label(self.master, text="Keyword Search criteria").pack()

        # Text box where journal entry is typed
        self.content_box = Text(self.master)
        self.content_box.pack()

        # Button to activate keyword search, linked to keyword_search function defined below
        Button(self.master, text="Keyword Search", width=10, command=self.keyword_search).pack()

        # Button to switch to instead do date search ***DEPRECATED RIGHT NOW***
        # Button(self.master, text="Take me to Date Search instead", width=10, command=self.date_search_instead).pack()

        # Next is date search label, entry boxes (one for each date, month, year), and button

    def keyword_search(self):
        """This function reads in titles and contents of all journal files into a dictionary list.
        Then it will see if keyword search criteria is contained in either the titles or content.
        Will return a list of journal entries which meet the criteria"""

        # For each file in directory, put title into key field of dictionary, content into value field
        path = "C:\\Users\\skyle\\OneDrive\\Documents\\DMACC\\CIS 189\\Final Project\\Journal Entries"
        self.file_names = os.listdir(path)

        titles_and_no_content_dictionary = dict.fromkeys(self.file_names)
        print(titles_and_no_content_dictionary)

        # GOOD TO THIS POINT! Need to add content to dictionary

        journal_contents = [0] * len(self.file_names)

        for j in range(0, len(self.file_names)):
            with open(self.file_names[j]) as f:
                journal_contents[j] = f.readlines()

        # Create dictionary from titles and content together
        titles_and_content_dictionary = dict(zip(titles_and_no_content_dictionary, journal_contents))

        print(titles_and_content_dictionary)

        # Search dictionary for keyword


        """for file_name in self.file_names:
            with open(file_name) as f:
                titles_and_content_dictionary.values(titles_and_content_dictionary[file_name]) = f.readlines()"""

        # messagebox.showinfo("Entry saved", "Journal entry saved successfully! ")
