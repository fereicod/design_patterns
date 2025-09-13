"""
This patter allows adding new functionalities to an object dynamically by wrapping it in "decorator" objects.
- OOP -> Abstraction
- SOLID -> SRP, OCP, LSP
"""
from abc import ABC, abstractmethod

class Coffee(ABC):
	@abstractmethod
	def get_cost(self) -> float: pass

	@abstractmethod
	def get_description(self) -> str: pass


class SimpleCoffee(Coffee):
	def get_cost(self) -> float: return 2.0
	def get_description(self) -> str: return "Simple coffee"


class CondimentDecorator(Coffee):
	def __init__(self, coffee: Coffee): 
		self._wrapped_coffee = coffee


class WithMilk(CondimentDecorator):
	def get_cost(self) -> float: 
		return self._wrapped_coffee.get_cost() + 0.5

	def get_description(self) -> str:
		return self._wrapped_coffee.get_description() + ", with milk"


print("--- Examples ---")
simple_coffee = SimpleCoffee()
my_coffee = WithMilk(simple_coffee)
print(f"{my_coffee.get_description()} -> cost: ${my_coffee.get_cost()}")