"""This Python file will contain the GUI details for the Journal app"""

#This program will generate a GUI titled Favorite Meal, which has four checkboxes. It will provide a response based on meal selected, and has an exit button to leave.
import tkinter as tk

'''
Define functions/methods below here
'''
#Function to open new window
def open_another_window(title):

    #Creating sub window
    sub_window = tk.Tk()
    sub_window.title = title

    return sub_window


def pick_new_entry():
    label.config(text="You clicked New Entry button")
    new_window = open_another_window("New Entry")
    new_entry = tk.Entry()
    new_entry.pack()
    new_entry.get()
    #new_window.create_window(200, 140, window=new_entry)"""

def pick_view_journal():
    label.config(text="You clicked View Journal button")


def pick_search_journal():
    label.config(text="You clicked Search button")


def pick_browse_entries():
    label.config(text="You clicked Browse Entries button")


def pick_rewind():
    label.config(text="You clicked Rewind button")


def pick_settings():
    label.config(text="You clicked Settings button")

'''
Define functions/methods above here
'''

#create main window
m = tk.Tk()
'''
Insert module code below here
'''
##The Main Window Title that appears in the bar
m.title('MyJournal') #replace this with whatever you would like

##Insert most of your main button code BELOW/between these --------------------------------------------------

### Create a text label, put it at bottom
label = tk.Label(m, text="No Selection Made") #label just displays Text
label.grid(row=7) #placing at 2nd from the bottom Row


### Create Buttons to Create New Entry, View Journal, Search Journal, Browse Entries, On this day (rewind), Settings
#Button 1
New_entry_button = tk.Button(m, text="Create new entry", width=25, command=pick_new_entry)
New_entry_button.grid(row=0)

#Button 2
View_journal_button = tk.Button(m, text="View journal", width=25, command=pick_view_journal)
View_journal_button.grid(row=1)

#Button 3
Search_button = tk.Button(m, text="Search journal", width=25, command=pick_search_journal)
Search_button.grid(row=2)

#Button 4
Browse_entries_button = tk.Button(m, text="Browse entries", width=25, command=pick_browse_entries)
Browse_entries_button.grid(row=3)

#Button 5
Rewind_button = tk.Button(m, text="On this day (rewind)", width=25, command=pick_rewind)
Rewind_button.grid(row=4)

#Button 6
Settings_button = tk.Button(m, text="Settings", width=25, command=pick_settings)
Settings_button.grid(row=5)


##Insert most of your main button code ABOVE/between these --------------------------------------------------

##The Main window Exit/destroy function; Note Feel free to change it's "text='Exit'" to another
##     word like "text='Quit'" or whatever is relevent for you; as well as modify the width
exit_button = tk.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)

'''
Insert module code above here
'''
m.mainloop()

"""
----------
[] CIS
----------
[] BIS
----------
row 2
----------
row 3
----------
"No Selection Made" (label)
----------
Exit (button)
----------"""