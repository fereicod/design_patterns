"""
This patter allows adding new functionalities to an object dynamically by wrapping it in "decorator" objects.
- OOP -> Abstraction
- SOLID -> SRP, OCP, LSP
"""
from abc import ABC, abstractmethod

# LSP: Common interface that allows a decorated coffee to be treated as a simple one.
class Coffee(ABC):
	@abstractmethod
	def get_cost(self) -> float: pass

	@abstractmethod
	def get_description(self) -> str: pass


# SRP: It's only responsability is to be a base coffee.
# OCP: This class is CLOSED for changes.
class SimpleCoffee(Coffee):
	def get_cost(self) -> float: return 2.0
	def get_description(self) -> str: return "Simple coffee"


class CondimentDecorator(Coffee):
	def __init__(self, coffee: Coffee): 
		self._wrapped_coffee = coffee


# SRP: It's only responsability is to add milk.
# OCP: This class is OPEN to new decorators.
class WithMilk(CondimentDecorator):
	def get_cost(self) -> float: 
		return self._wrapped_coffee.get_cost() + 0.5

	def get_description(self) -> str:
		return self._wrapped_coffee.get_description() + ", with milk"

# SRP: It's only responsability is to add chocolate.
# OCP: This class is OPEN to new decorators.
class WithChocolate(CondimentDecorator):
	def get_cost(self) -> float: 
		return self._wrapped_coffee.get_cost() + 1.0

	def get_description(self) -> str:
		return self._wrapped_coffee.get_description() + ", with chocolate"


print("--- Examples ---")
simple_coffee = SimpleCoffee()

my_coffee_with_milk = WithMilk(simple_coffee)
print(f"{my_coffee_with_milk.get_description()} -> cost: ${my_coffee_with_milk.get_cost()}")

my_coffee_with_choco = WithChocolate(simple_coffee)
print(f"{my_coffee_with_choco.get_description()} -> cost: ${my_coffee_with_choco.get_cost()}")

my_coffee_with_milk_choco = WithMilk(WithChocolate(simple_coffee)) #WithChocolate(WithMilk(simple_coffee))
print(f"{my_coffee_with_milk_choco.get_description()} -> cost: ${my_coffee_with_milk_choco.get_cost()}")

my_coffee_with_milk_choco = WithMilk(my_coffee_with_choco) #WithChocolate(my_coffee_with_milk)
print(f"{my_coffee_with_milk_choco.get_description()} -> cost: ${my_coffee_with_milk_choco.get_cost()}")