"""This python file will contain the Journal class which contains several special methods"""

#imports?
import csv
from datetime import datetime as dt


class Journal:
    """journal class"""
    def __init__(self, entry_title, entry_content, creation_date=dt.now()):
        self.date = creation_date
        self.title = entry_title
        self.entry = entry_content

    # Method to update title
    def change_title(self, new_title):
        self.title = new_title

    # Method to update entry
    def change_entry(self, updated_entry):
        self.entry = updated_entry

    def write_entry_to_file(self):
        """f = open("journal.txt", "a")
        f.write(self.date + '\n')
        f.close()"""

        with open('journal.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow([self.date, self.title, self.entry])
            #writer.writerow([1, "Ash Ketchum", "English"])
            #writer.writerow([2, "Gary Oak", "Mathematics"])
            #writer.writerow([3, "Brock Lesner", "Physics"])

    # Display method
    def display(self):
        return "Date: " + str(self.date) + '\n' + "Title: " + str(self.title) + '\n' + 'Entry: ' + str(self.entry)


if __name__ == "__main__":
    e = Journal('Interesting Title', 'Hello world!')
    print(e.display())
    e.write_entry_to_file()
    e.change_title('Better Title')
    e.change_entry('Goodbye world')
    print(e.display())
    e.write_entry_to_file()
    del e #Garbage collection