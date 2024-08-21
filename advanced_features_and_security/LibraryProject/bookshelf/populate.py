# Import the models
from bookshelf.models import Author, Book, Library, Librarian, CustomUser, UserProfile
from django.contrib.auth.models import Permission
from django.db import IntegrityError

# Add Custom Users
user1 = CustomUser.objects.create_user(
    email="admin@example.com",
    password="adminpassword",
    date_of_birth="1990-01-01",
    profile_picture=None,  # Assuming no initial profile picture
    is_staff=True,
    is_superuser=True
)

user2 = CustomUser.objects.create_user(
    email="user@example.com",
    password="userpassword",
    date_of_birth="1992-06-15",
    profile_picture=None
)

# Create User Profiles
UserProfile.objects.create(user=user1, role='Admin')
UserProfile.objects.create(user=user2, role='Member')

# Add authors
author1 = Author.objects.create(name="George Orwell")
author2 = Author.objects.create(name="Harper Lee")
author3 = Author.objects.create(name="Jane Austen")
author4 = Author.objects.create(name="F. Scott Fitzgerald")
author5 = Author.objects.create(name="Herman Melville")
author6 = Author.objects.create(name="J.K. Rowling")
author7 = Author.objects.create(name="J.R.R. Tolkien")
author8 = Author.objects.create(name="George R.R. Martin")
author9 = Author.objects.create(name="Agatha Christie")
author10 = Author.objects.create(name="Mark Twain")

# Add books for each author
Book.objects.create(title="1984", author=author1)
Book.objects.create(title="Animal Farm", author=author1)
Book.objects.create(title="Homage to Catalonia", author=author1)

Book.objects.create(title="To Kill a Mockingbird", author=author2)
Book.objects.create(title="Go Set a Watchman", author=author2)

Book.objects.create(title="Pride and Prejudice", author=author3)
Book.objects.create(title="Sense and Sensibility", author=author3)
Book.objects.create(title="Emma", author=author3)

Book.objects.create(title="The Great Gatsby", author=author4)
Book.objects.create(title="Tender is the Night", author=author4)
Book.objects.create(title="This Side of Paradise", author=author4)

Book.objects.create(title="Moby Dick", author=author5)
Book.objects.create(title="Bartleby, the Scrivener", author=author5)
Book.objects.create(title="Billy Budd, Sailor", author=author5)

Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author6)
Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author6)

Book.objects.create(title="The Hobbit", author=author7)
Book.objects.create(title="The Lord of the Rings", author=author7)

Book.objects.create(title="A Game of Thrones", author=author8)
Book.objects.create(title="A Clash of Kings", author=author8)

Book.objects.create(title="Murder on the Orient Express", author=author9)
Book.objects.create(title="And Then There Were None", author=author9)

Book.objects.create(title="The Adventures of Tom Sawyer", author=author10)
Book.objects.create(title="The Adventures of Huckleberry Finn", author=author10)

# Add libraries
library1 = Library.objects.create(name="Chiron Library")
library2 = Library.objects.create(name="Veyron Library")
library3 = Library.objects.create(name="Divo Library")
library4 = Library.objects.create(name="Centodieci Library")
library5 = Library.objects.create(name="Bolide Library")

# Add books to libraries
library1.books.add(Book.objects.get(title="1984"))
library1.books.add(Book.objects.get(title="The Great Gatsby"))
library2.books.add(Book.objects.get(title="Pride and Prejudice"))
library2.books.add(Book.objects.get(title="To Kill a Mockingbird"))
library3.books.add(Book.objects.get(title="The Adventures of Huckleberry Finn"))
library3.books.add(Book.objects.get(title="Murder on the Orient Express"))
library4.books.add(Book.objects.get(title="Harry Potter and the Philosopher's Stone"))
library4.books.add(Book.objects.get(title="The Lord of the Rings"))
library5.books.add(Book.objects.get(title="A Game of Thrones"))
library5.books.add(Book.objects.get(title="Moby Dick"))

# Add librarians
librarian1 = Librarian.objects.create(name="Zinedine Zidane", library=library1)
librarian2 = Librarian.objects.create(name="Raúl González", library=library2)
librarian3 = Librarian.objects.create(name="Iker Casillas", library=library3)
librarian4 = Librarian.objects.create(name="Cristiano Ronaldo", library=library4)
librarian5 = Librarian.objects.create(name="Alfredo Di Stéfano", library=library5)

# Associate Librarians with Users (optional, if needed)
# librarian1.user = user2
# librarian1.save()

# Assign a permission to a user
permission = Permission.objects.get(codename='can_add_book')
user2.user_permissions.add(permission)

# Testing Queries (optional, for verification)
books_in_chiron_library = library1.books.all()
print([book.title for book in books_in_chiron_library])

# Integrity Checks (optional)
try:
    Book.objects.create(title="Duplicate Book", isbn="1234567890123", author=author1)
except IntegrityError as e:
    print("Integrity error:", e)

# Additional Library Data (optional)
library1.description = "A serene environment for classic literature lovers."
library1.location = "123 Chiron St, Fiction City"
library1.save()
