class Library:
    def __init__(self):
        # make sets for different genres
        self.Fiction = set()
        self.Non_Fiction = set()
        self.Science = set()
        self.History = set()

    def add_book(self, genre, book):
        if genre == "Fiction":
            self.Fiction.add(book)
        elif genre == "Non-Fiction":
            self.Non_Fiction.add(book)
        elif genre == "Science":
            self.Science.add(book)
        elif genre == "History":
            self.History.add(book)
        else:
            print(f"Genre '{genre}' does not exist.")

    def remove_book(self, genre, book):
        if genre == "Fiction":
            self.Fiction.discard(book)
        elif genre == "Non-Fiction":
            self.Non_Fiction.discard(book)
        elif genre == "Science":
            self.Science.discard(book)
        elif genre == "History":
            self.History.discard(book)
        else:
            print(f"Genre '{genre}' does not exist.")

    def book_exists(self, genre, book):
        if genre == "Fiction":
            return book in self.Fiction
        elif genre == "Non-Fiction":
            return book in self.Non_Fiction
        elif genre == "Science":
            return book in self.Science
        elif genre == "History":
            return book in self.History
        else:
            print(f"Genre '{genre}' does not exist.")
            return False

    def union_books(self, genres):
        selected_genres = []
        for genre in genres:
            if genre == "Fiction":
                selected_genres.append(self.Fiction)
            elif genre == "Non-Fiction":
                selected_genres.append(self.Non_Fiction)
            elif genre == "Science":
                selected_genres.append(self.Science)
            elif genre == "History":
                selected_genres.append(self.History)
            else:
                print(f"Genre '{genre}' does not exist.")

        # return the union of all selected genres
        return set().union(*selected_genres)

    def intersection_books(self, genres):
        selected_genres = []
        for genre in genres:
            if genre == "Fiction":
                selected_genres.append(self.Fiction)
            elif genre == "Non-Fiction":
                selected_genres.append(self.Non_Fiction)
            elif genre == "Science":
                selected_genres.append(self.Science)
            elif genre == "History":
                selected_genres.append(self.History)
            else:
                print(f"Genre '{genre}' does not exist.")

        # return the intersection of all selected genres
        return set.intersection(*selected_genres)

    def difference_books(self, genre1, genre2):
        if genre1 == "Fiction" and genre2 == "Non-Fiction":
            return self.Fiction.difference(self.Non_Fiction)
        elif genre1 == "Non-Fiction" and genre2 == "Fiction":
            return self.Non_Fiction.difference(self.Fiction)
        elif genre1 == "Science" and genre2 == "History":
            return self.Science.difference(self.History)
        elif genre1 == "History" and genre2 == "Science":
            return self.History.difference(self.Science)
        else:
            print(f"Invalid genre comparison between '{genre1}' and '{genre2}'")
            return set()


# making instance of Library Class
library = Library()

# add books
library.add_book("Fiction", "The Great Gatsby")
library.add_book("Fiction", "1984")
library.add_book("Science", "A Brief History of Time")
library.add_book("History", "The History of the Ancient World")

# check if a book exists in a genre
print("\nBook 1984 exist in Fiction? ", library.book_exists("Fiction", "1984"))
print("\nBook 1984 exist in Science? ", library.book_exists("Science", "1984"))

# remove a book from a genre
print("\nRemoving 1984 from Fiction")
library.remove_book("Fiction", "1984")
print("Book 1984 exist in Fiction? ", library.book_exists("Fiction", "1984"))

# perform set operations
print("\nUnion of Fiction and Science:\n", library.union_books(["Fiction", "Science"]))
print("\nIntersection of Fiction and Science:\n", library.intersection_books(["Fiction", "Science"]))
print("\nIntersection of Fiction and Science:\n", library.difference_books("Fiction", "History"))
