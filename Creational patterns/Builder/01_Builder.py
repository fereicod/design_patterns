"""
This pattern separates the construcion of a complex object from it's representation, allowing the same construction
pricess to create different representations.
- SOLID -> SRP, OCP, DIP
"""
from abc import ABC, abstractmethod

class Computer:
	def __init__(self):
		self.parts: list[str] = []

	def add(self, part):
		self.parts.append(part)

	def show(self):
		print("Computer:", ", ".join(self.parts))


class Builder(ABC):
	@abstractmethod
	def build_cpu(self): pass

	@abstractmethod
	def build_gpu(self): pass

	@abstractmethod
	def get_result(self) -> Computer: pass


class GamingPCBuilder(Builder):
	def __init__(self):
		self.computer = Computer()

	def build_cpu(self): self.computer.add("High-end CPU")
	def build_gpu(self): self.computer.add("RTX GPU")
	def get_result(self): return self.computer

class OfficePCBuilder(Builder):
	def __init__(self):
		self.computer = Computer()

	def build_cpu(self): self.computer.add("Basic CPU")
	def build_gpu(self): self.computer.add("Integrated GPU")
	def get_result(self): return self.computer 


class Director:
	def __init__(self, builder: Builder):
		self.builder = builder

	def constructor(self):
		self.builder.build_cpu()
		self.builder.build_gpu()
		return self.builder.get_result()


print("--- Examples ---")
pc1 = Director(GamingPCBuilder()).constructor()
pc1.show()

pc2 = Director(OfficePCBuilder()).constructor()
pc2.show()
