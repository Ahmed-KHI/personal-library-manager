import json

def main():
    library = []
    
    def display_menu():
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

    def add_book():
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        publication_year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read_status_input = input("Have you read this book? (yes/no): ").strip().lower()
        read_status = True if read_status_input == 'yes' else False
        
        book = {
            'title': title,
            'author': author,
            'publication_year': publication_year,
            'genre': genre,
            'read_status': read_status
        }
        library.append(book)
        print("Book added successfully!")

    def remove_book():
        title = input("Enter the title of the book to remove: ")
        for book in library:
            if book['title'].lower() == title.lower():
                library.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found.")

    def search_book():
        print("Search by:")
        print("1. Title")
        print("2. Author")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter the title: ")
            matches = [book for book in library if title.lower() in book['title'].lower()]
        elif choice == '2':
            author = input("Enter the author: ")
            matches = [book for book in library if author.lower() in book['author'].lower()]
        else:
            print("Invalid choice.")
            return
        
        if matches:
            print("Matching Books:")
            for book in matches:
                read_status = "Read" if book['read_status'] else "Unread"
                print(f"{book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")
        else:
            print("No matching books found.")

    def display_all_books():
        if not library:
            print("Your library is empty.")
            return
        
        print("Your Library:")
        for book in library:
            read_status = "Read" if book['read_status'] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")

    def display_statistics():
        total_books = len(library)
        if total_books == 0:
            print("No books in the library to display statistics.")
            return
        
        read_books = sum(1 for book in library if book['read_status'])
        percentage_read = (read_books / total_books) * 100
        
        print(f"Total books: {total_books}")
        print(f"Percentage read: {percentage_read:.1f}%")

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_all_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def load_library_from_file(filename='library.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding the library file. Starting with an empty library.")
        return []

def save_library_to_file(library, filename='library.json'):
    with open(filename, 'w') as file:
        json.dump(library, file, indent=4)

if __name__ == "__main__":
    library = load_library_from_file()
    main()
    save_library_to_file(library)
    print("Library saved to file. Goodbye!")