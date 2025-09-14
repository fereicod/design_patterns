"""
Loan Products (FinTech)
A simple loan can be "decorated" with add-ons like insurance or an immediate withdrawal service, each adding to the cost.
"""
from abc import ABC, abstractmethod

# LSP: The base interface that allows for substitution.
class FinancialProduct(ABC):
	@abstractmethod
	def get_monthly_cost(self) -> float: pass
	@abstractmethod
	def get_description(self) -> str: pass

# SRP: It's just a simple loan.
# OCP: CLOSED for chages.
class SimpleLoan(FinancialProduct):
	def __init__(self, amount: float):
		self._amount = amount

	def get_monthly_cost(self) -> float:
		return self._amount / 12

	def get_description(self) -> str:
		return f"Base loan of ${self._amount}"


class BenefitDecorator(FinancialProduct):
	def __init__(self, product: FinancialProduct):
		self._wrapped_product = product


# SRP: Only adds the insurance responsability
# OCP: OPEN for extension.
class WithLifeInsurance(BenefitDecorator):
	def get_monthly_cost(self) -> float:
		return self._wrapped_product.get_monthly_cost() + 200

	def get_description(self) -> str:
		return self._wrapped_product.get_description() + " + Life Insurance"


print("--- Example ---")
my_loan = WithLifeInsurance(SimpleLoan(6000))
print(f"Product: {my_loan.get_description()}, Monthly Payment: ${my_loan.get_monthly_cost():.2f}")
