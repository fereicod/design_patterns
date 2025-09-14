"""
Payment Processor (Fintech)
A payment gasteway needs to create different "processor" objects depending on the payment method (Card, Bank Transfer, etc.) without coupling the main code to them.
"""
from abc import ABC, abstractmethod

# Products
class PaymentProcessor(ABC):
	@abstractmethod
	def process(self, amount: float): pass

class CreditCardProcessor(PaymentProcessor):
	def process(self, amount: float):
		print(f"Processing ${amount} with Credit Card")

class BankTransferProcessor(PaymentProcessor):
	def process(self, amount: float):
		print(f"Processing ${amount} with Bank Transfer")


# Creators (Factories)
# DIP: High-level code will depend on this abstraction.
class PaymentGateway(ABC):
	# OCP: The "execute_payment" logic is generico and doesn't change is CLOSED.
	def execute_payment(self, amount: float):
		print(f"Initiating payment for ${amount} through the gateway")
		# DIP: It delegates the logic object creation to the factory method
		processor = self.create_processor()
		processor.process(amount)

	# The Factory Method
	@abstractmethod
	def create_processor(self) -> PaymentProcessor: pass

# OCP: OPEN for extension with new gateway types.
class CardGateway(PaymentGateway):
	def create_processor(self) -> PaymentProcessor:
		return CreditCardProcessor()

class BankTransferGateway(PaymentGateway):
	def create_processor(self) -> PaymentProcessor:
		return BankTransferProcessor()


print("--- Example ---")
card_gateway = CardGateway()
card_gateway.execute_payment(500.00)
print("")
bank_gateway = BankTransferGateway()
bank_gateway.execute_payment(200.00)