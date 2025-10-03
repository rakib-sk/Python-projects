#create a class name is libararl
class Book:
	def __init__(self,title,author,price):
		self.title = title
		self.author = author
		self.price = price 
	#Create display_info function
	def display_info(self):
		print(f"Title: {self.title}")
		print(f"Author: {self.author}")
		print(f"Price: {self.price} TK")
		print( )
#=====================================
#Create Ebook class inherit Book
class Ebook(Book):
	def __init__(self,Title,Author,Price,file_size):
		self.title = Title
		self.author = Author
		self.price = Price
		self.file_size = file_size
	def display_info(self):
		print(f"Title: {self.title}")
		print(f"Author: {self.author}")
		print(f"Price: {self.price} TK")
		print(f"file size: {self.file_size} MB")
		print()
#========================================
#create library class
class Library:
	def __init__(self):
		self.book = []
	def add_book(self,book):
		self.book.append(book)
	def show_book(self):
		for book in self.book:
			book.display_info()
#========================================
#create book objects
book1 = Book("Python Basics", "John Smith", 350)
book2 = Book("OOP Concepts", "Maria Khan", 450)
book3 = Book("Data Structures in Python", "David Lee", 500)
book4 = Book("Machine Learning Intro", "Andrew Ng", 650)
book5 = Book("Web Development Crash Course", "Colt Steele", 700)
book6 = Book("C Programming for Beginners", "Dennis Ritchie", 400)
book7 = Book("Java Complete Guide", "Herbert Schildt", 750)
book8 = Book("Database Management", "Abraham Silberschatz", 800)
book9 = Book("Operating System Concepts", "Silberschatz & Galvin", 950)
book10 = Book("Computer Networks", "Andrew S. Tanenbaum", 900)


ebook1 = Ebook("Cloud IT Solution (4th Edition)", "Md. Al-Amin Nipu, Md. Mehedi Hassan", 904, 5)
ebook2 = Ebook("Artificial Intelligence Basics", "Stuart Russell", 600, 8)
ebook3 = Ebook("Deep Learning with Python", "Francois Chollet", 1200, 12)
ebook4 = Ebook("Cyber Security Essentials", "William Stallings", 700, 6)
ebook5 = Ebook("DevOps Handbook", "Gene Kim", 850, 9)
ebook6 = Ebook("Ethical Hacking Guide", "Jon Erickson", 950, 7)
ebook7 = Ebook("JavaScript: The Good Parts", "Douglas Crockford", 550, 4)
ebook8 = Ebook("React.js in Action", "Mark Tielens Thomas", 800, 10)
ebook9 = Ebook("Kubernetes Up & Running", "Kelsey Hightower", 1000, 15)
ebook10 = Ebook("Cloud Native Architecture", "Bill Wilder", 1100, 11)

# =========================
# Library setup
# =========================
my_library = Library()


my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)
my_library.add_book(book6)
my_library.add_book(book7)
my_library.add_book(book8)
my_library.add_book(book9)
my_library.add_book(book10)


my_library.add_book(ebook1)
my_library.add_book(ebook2)
my_library.add_book(ebook3)
my_library.add_book(ebook4)
my_library.add_book(ebook5)
my_library.add_book(ebook6)
my_library.add_book(ebook7)
my_library.add_book(ebook8)
my_library.add_book(ebook9)
my_library.add_book(ebook10)

# Show all books
my_library.show_book()