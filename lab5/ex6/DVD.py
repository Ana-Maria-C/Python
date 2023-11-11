from ex6.LibraryItem import LibraryItem


class DVD(LibraryItem):
    def __init__(self, title, director, itemID, runtime):
        super().__init__(title, director, itemID)
        self.runtime = runtime

    def display_details(self):
        super().display_details()
        print("Runtime: {}".format(self.runtime))