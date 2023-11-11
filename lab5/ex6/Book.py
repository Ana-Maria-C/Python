from ex6.LibraryItem import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, author, itemID, numPages, genre, publicationDate):
        super().__init__(title, author, itemID)
        self.numPages = numPages
        self.genre = genre
        self.publicationDate = publicationDate

    def display_details(self):
        super().display_details()
        print("Number of Pages: {}".format(self.numPages))
        print("Genre: {}".format(self.genre))
        print("Publication Date: {}".format(self.publicationDate))