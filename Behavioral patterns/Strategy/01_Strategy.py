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

	def execute(self, data: list) -> None:
		result = self._strategy.sort(data)
		print(result)


class BubbleSortStrategy(SortingStrategy):
	def sort(self, data: list) -> list:
		print("- Sorting with Bubble Sort...")
		return sorted(data)


print("--- Examples ---")
bubble_sort = BubbleSortStrategy()
context = SortingContext(bubble_sort)
context.execute([5,2,8])
