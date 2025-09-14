"""
Assessment Generator (HR Tech)
X's ATS needs to generate different types of assessments for candidates depending on the role (coding test, portfolio review, psychometric test).
"""
from abc import ABC, abstractmethod

# Products
class Assesment(ABC):
	@abstractmethod
	def send_to_candidate(self, email) -> str: pass

class PythonCodingTest(Assesment):
	def send_to_candidate(self, email: str) -> str:
		print(f"Sending Python coding test to {email} via HackerRank.")

class PortfolioReview(Assesment):
	def send_to_candidate(self, email: str) -> str:
		print(f"Requesting {email} to submit their Behance portfolio.")


# Creators (Factories)
# DIP: Abstraction for the assessment creator.
class AssessmentCreator(ABC):
	# OCP: The assignment logic is generic and does not change CLOSED.
	def assing_to_candidate(self, email: str):
		print(F"Assigning assessment to candidate {email}")
		# DIP: Creation is delegated to the factory method
		assesment = self.create_assessment()
		assesment.send_to_candidate(email)

	# The Factory Method
	@abstractmethod
	def create_assessment(self) -> Assesment: pass


# OCP: OPEN for extension for new job type
class PythonDevCreator(AssessmentCreator):
	def create_assessment(self) -> Assesment:
		return PythonCodingTest()

class UXDesignerCreator(AssessmentCreator):
	def create_assessment(self) -> Assesment:
		return PortfolioReview()


print("--- Example --")
dev_creator = PythonDevCreator()
dev_creator.assing_to_candidate("mferna.92@gmail.com")
print("")
ux_creator = UXDesignerCreator()
ux_creator.assing_to_candidate("mferna.92@outlook.com")