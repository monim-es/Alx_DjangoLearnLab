#Query all books by a specific author.
>>> from relationship_app.models import Author, Book
>>> author = Author.objects.get(name='es')        
>>> author
<Author: es>
>>> books = Book.objects.filter(author=author)
>>> books
<QuerySet [<Book: winter days>]>
>>>

#List all books in a library.
>>> from relationship_app.models import Library, Book
>>> library = Library.objects.get(name='reading library') 
>>> library
<Library: reading library>
>>> books = library.books.all()
>>> books
<QuerySet [<Book: summer days>, <Book: winter days>]>
>>>
# Retrieve the librarian for a library.

>>> from relationship_app.models import Library, Librarian
>>> library = Library.objects.get(name='reading library')       
>>> library
<Library: reading library>
>>> librarian = library.librarian 
>>> librarian
<Librarian: esLab>
>>>