from ex6.LibraryItem import LibraryItem


class Magazine(LibraryItem):
    def __init__(self, title, itemID, issueNumber, publicationDate):
        super().__init__(title, "Unknown", itemID)
        self.issueNumber = issueNumber
        self.publicationDate = publicationDate

    def display_details(self):
        super().display_details()
        print("Issue Number: {}".format(self.issueNumber))
        print("Publication Date: {}".format(self.publicationDate))
