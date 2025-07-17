from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    print(f"\nBooks by author: {author_name}")
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(f"- {book.title}")

def list_books_in_library(library_name):
    print(f"\nBooks in library: {library_name}")
    books = Book.objects.filter(library__name=library_name)
    for book in books:
        print(f"- {book.title} (Author: {book.author.name})")

def get_librarian_for_library(library_name):
    print(f"\nLibrarian for library: {library_name}")
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        print(f"Librarian: {librarian.name}")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")
