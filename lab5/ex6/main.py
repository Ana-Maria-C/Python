from ex6.DVD import DVD
from ex6.Magazine import Magazine
from ex6.Book import Book


def main():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1, 310, "Fantasy", "21/09/1937")
    book.display_details()
    book.check_out()
    print()
    book.display_details()
    print()

    magazine = Magazine("National Geographic", 2, 1, "October 1888")
    magazine.display_details()
    print()

    dvd = DVD("The Matrix", "The Wachowskis", 3, 136)
    dvd.display_details()
    print()


if __name__ == "__main__":
    main()