"""
Interest Rate Calculation (FinTech)
A FinTech might have different models (strategies) to calculate a loan's interest rate.
"""
from abc import ABC, abstractmethod

# DIP: Abstraction that the context and strategies depend on.
class RateStrategy(ABC):
	@abstractmethod
	def calculate_rate(self, credit_score: int) -> float: pass


# SRP: It's only responsability is the calculation for low-risk profiles.
class LowRiskRateStrategy(RateStrategy):
	def calculate_rate(self, score: int) -> float:
		print("Using low-risk rate model.")
		return 15.5

# OCP: The calculator is CLOSED for changes
class OfferCalculator:
	# DIP: Depends on the RateStrategy abstraction.
	def __init__(self, strategy: RateStrategy):
		self._strategy = strategy

	def generate_offer(self, client: dict):
		rate = self._strategy.calculate_rate(client["score"])
		print(f"Offer for {client["name"]}: Rate of {rate}%")


print("--- Examples ---")
calculator = OfferCalculator(LowRiskRateStrategy())
calculator.generate_offer({
		"name": "Fer",
		"score": 780
	})