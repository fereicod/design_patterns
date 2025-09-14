"""
When a "subject" changes, all others "observers" are notified automatically.
- SOLID -> SRP, OCP, DIP
"""
from abc import ABC, abstractmethod

# DIP: Store depends on this abstraction, not on concrete implementations.
class Observer(ABC):
	@abstractmethod
	def update(self, order_info: str): pass


# OCP: We can add more notifiers without modifying Store.
class EmailNotifier(Observer):
	def update(self, order_info: str):
		print(f"Email sent: Order {order_info}")

class SMSNotifier(Observer):
	def update(self, order_info: str):
		print(f"SMS sent: Order {order_info}")


# SRP: Store only manages observers and notifications.
class Store:
	def __init__(self):
		self._observers = []

	def attach(self, obs: Observer):
		self._observers.append(obs)

	def notify(self, order_info: str):
		for obs in self._observers:
			obs.update(order_info)

	def new_order(self, order_info: str):
		print(f"Store: New order -> {order_info}")
		self.notify(order_info)


print("--- Examples ---")
store = Store()
store.attach(EmailNotifier())
store.attach(SMSNotifier())

store.new_order("ID#1001 - Laptop")