"""
Provides a simplified, unified interface to a set of interfaces in a complex subsystem.
- OOP -> Encapsulation
- SOLID -> SRP, DIP
"""
class CPU:
	def execute(self): print("CPU: Executing...")

class RAM:
	def load(self): print("RAM: Loading data...")


# SRP: The facade's only responsability is to simplify startup.
# DIP: The client will depend on this simple facade, not the complex subsystem.
class ComputerFacade:
	def __init__(self):
		self.cpu, self.ram = CPU(), RAM()

	def start(self):
		self.ram.load()
		self.cpu.execute()


print("--- Examples ---")
computer = ComputerFacade()
computer.start()