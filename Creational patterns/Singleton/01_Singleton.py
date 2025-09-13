"""
This pattern ensures a class has only one instance and provides a global point of access to it.
- SOLID -> SRP, DIP
"""

# SRP: Handles instance creation only
# DIP: Clients depend on abstraction, not concrete instantiation
class SingletonMeta(type):
	_instance = None
	def __call__(cls, *args, **kwargs):
		if cls._instance is None:
			print("Creating a new Singleton instance...")
			cls._instance = super().__call__(*args, **kwargs)
		return cls._instance

class Singleton(metaclass=SingletonMeta):
	def __init__(self):
		self.value = 42 # Example attribute

	def business_logic(self):
		print("Executing business logic in the seingleton.")


print("--- Examples ---")
s1 = Singleton()
s2 = Singleton()

s1.business_logic()

# Both variable point to the same instance
print("s1 is s2:", s1 is s2)