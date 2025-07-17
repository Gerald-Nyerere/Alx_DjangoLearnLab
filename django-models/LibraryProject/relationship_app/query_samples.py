from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    print(f"\nBooks by author: {author_name}")
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(f"- {book.title}")

def list_books_in_library(library_name):
    print(f"\nBooks in library: {library_name}")
    try:
        library = Library.objects.get(name=library_name)  # Explicit use
        books = library.books.all()  # Explicit use (requires related_name='books' in Book model)
        for book in books:
            print(f"- {book.title} (Author: {book.author.name})")
    except Library.DoesNotExist:
        print("Library not found.")

def get_librarian_for_library(library_name):
    print(f"\nLibrarian for library: {library_name}")
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian: {librarian.name}")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")
