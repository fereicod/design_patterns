"""
This pattern allows defining a family algorithms, putting each in a separatec lass, and making them interchangeable.
- OOP -> Polymorphism
- SOLID -> SRP, OCP, DIP
"""
from abc import ABC, abstractmethod


# DIP: This is the abstraction everyone depends on.
class SortingStrategy(ABC):
	@abstractmethod
	def sort(self, data: list) -> list: pass


# SRP: It's only responsability is to coordinate.
# OCP: This class is CLOSED for change.
class SortingContext:
	# DIP: It depends on the abstraction, not a concrete strategy.
	def __init__(self, strategy: SortingStrategy):
		self._strategy = strategy

	@property
	def strategy() -> SortingStrategy:
		return self._strategy

	@strategy.setter
	def strategy(self, strategy: SortingStrategy) -> None:
		self._strategy = strategy

	def execute(self, data: list) -> None:
		result = self._strategy.sort(data)
		print(result)


# SRP: These classes only resopnsability is to sort with their methods.
# OCP: The system is OPEN to new strategies.
class BubbleSortStrategy(SortingStrategy):
	def __init__(self): print("= BubbleSort =")

	def sort(self, data: list) -> list:
		return sorted(data)

class QuickSortStrategy(SortingStrategy):
	def __init__(self): print("= QuickSort =")

	def sort(self, data: list) -> list:
		return sorted(data)


print("--- Examples ---")
context = SortingContext(BubbleSortStrategy())
context.execute([5,2,8])

context.strategy = QuickSortStrategy()
context.execute([6,4,9])


