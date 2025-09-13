"""
Defines an interface for creating an object, but lets subclasses alter the type of objects that will be crearted.
- SOLID -> OCP, DIP
"""
from abc import ABC, abstractmethod

# Products
class Document(ABC):
	@abstractmethod
	def open(self): pass

class TextDocument(Document):
	def open(self): print("Opening text document.")

class PDFDocument(Document):
	def open(self): print("Openning pdf document.")


# Creators (Factories)
# DIP: The client code will depend on this abstraction
class Application(ABC):
	# OCP:The logic of 'new_document' is CLOSED for change
	def new_document(self):
		print("Common logic: opening a new document in the app.")
		# DIP: It depends on the abstract 'factory_method' to create the product.
		doc = self.create_document()
		doc.open()

	# This is the Factory method
	@abstractmethod
	def create_document(self) -> Document: pass


# OCP: The system is OPEN to new creator implementations.
class TextApplication(Application):
	def create_document(self) -> Document:
		print("TextApplication: Creating a text document.")
		return TextDocument()

class PDFApplication(Application):
	def create_document(self) -> Document:
		print("PDFApplication: Creating a pdf document.")
		return PDFDocument()

print("--- Examples ---")
text_app = TextApplication()
text_app.new_document()
print("")
pdf_app = PDFApplication()
pdf_app.new_document()