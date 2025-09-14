"""
Transaction Notifications (FinTech)
"""
from abc import ABC, abstractmethod

# DIP: Key abstractions.
class Observer(ABC):
	@abstractmethod
	def update(self, subject): pass

class Subject(ABC):
	@abstractmethod
	def register_observer(self, observer: Observer): pass
	@abstractmethod
	def notify_observers(self): pass


# OCP: This class is CLOSED for changes if new observers are added.
class PaymentProcessor(Subject):
	_observers: list[Observer] = []
	_last_payment: dict = None
	
	# DIP: Depends on the Observer abstraction, not concrete classes.
	def register_observer(self, observer: Observer):
		self._observers.append(observer)

	def notify_observers(self):
		for observer in self._observers:
			observer.update(self)

	def process_payment(self, payment: dict):
		self._last_payment = payment
		self.notify_observers()

	def get_last_payment(self) -> dict:
		return self._last_payment


# OCP: The system is OPEN for extansion with new observers.
class FraudMonitor(Observer):
	def update(self, subject: PaymentProcessor):
		if subject.get_last_payment()["amount"] > 20000:
			print("-> FraudMonitor: ALERT!")


print("--- Examples ---")
processor = PaymentProcessor()
processor.register_observer(FraudMonitor())
processor.process_payment({"amount": 25000})