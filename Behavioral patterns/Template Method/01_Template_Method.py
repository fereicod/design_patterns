"""
This pattern defines the skeleton of an algorithm in a base class but lets subclasses override specific steps.
- OOP -> Inheritance
- SOLID -> OCP, DIP
"""

from abc import ABC, abstractmethod

class BeveragePreparer(ABC):
	def prepare(self):
		self.boil_water()
		self.brew_ingredient()
		self.pour_in_cup()
		self.add_condiments()

	def boil_water(self): print("Boiling water")
	def pour_in_cup(self): print("Pouring into cup")

	@abstractmethod
	def brew_ingredient(self): pass
	@abstractmethod
	def add_condiments(self): pass


class TeaPreparer(BeveragePreparer):
	def __init__(self): print("= Tea =")
	def brew_ingredient(self): print("Steeping the teabag")
	def add_condiments(self): print("Adding lemon")

print("--- Examples ---")
tea = TeaPreparer()
tea.prepare()


