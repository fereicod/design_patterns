"""
This pattern allows defining a family algorithms, putting each in a separatec lass, and making them interchangeable.
- OOP -> Polymorphism
- SOLID -> SRP, OCP, DIP
"""
from abc import ABC, abstractmethod


class SortingStrategy(ABC):
	@abstractmethod
	def sort(self, data: list) -> list: pass


class SortingContext:
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


