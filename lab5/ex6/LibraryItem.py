from datetime import datetime, timedelta


class LibraryItem:
    def __init__(self, title, author, itemID):
        self.title = title
        self.author = author
        self.itemID = itemID
        self.onLoan = False
        self.dueDate = datetime.now()

    def check_out(self):
        if self.onLoan:
            print("Sorry, this item is already on loan")
        else:
            self.onLoan = True
            self.dueDate = datetime.now() + timedelta(weeks=3)

    def return_item(self):
        self.onLoan = False
        self.dueDate = datetime.now()

    def display_details(self):
        print("Library Item ID: {}".format(self.itemID))
        print("Library Item Title: {}".format(self.title))
        print("Library Item Author: {}".format(self.author))
        print("On Loan: {}".format(self.onLoan))
        print("Due Date: {}".format(self.dueDate))