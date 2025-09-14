"""
Application Processor (FinTech)
The flow for processing different financial applications (loan, new client) is similar: receive, validate, process, and save.
"""
from abc import ABC, abstractmethod

class ApplicationProcessor(ABC):
	# OCP: This template method is CLOSED for modification.
	def process_application(self, data: dict):
		application = self.parse_data(data)
		# DIP: It depends on the "validate_format" and "enrich_data" abstractions.
		if self.validate_format(application):
			self.enrich_data(application)
			self.save_result(application)
			print(f"Application {application["id"]} processed successfully")
		else:
			print(f"Validation error in application {application["id"]}")

	def parse_data(self, data: dict) -> dict: return data
	
	def save_result(self, application: dict):
		print(f"Saving result for {application["id"]} in DB")

	# OCP: The system is OPEN for extension by implementing these methods.
	@abstractmethod
	def validate_format(self, application: dict) -> bool: pass
	@abstractmethod
	def enrich_data(self, application: dict): pass


class LoanApplicationProcessor(ApplicationProcessor):
	def validate_format(self, app: dict) -> bool: 
		return "amount" in app and "term" in app

	def enrich_data(self, app: dict):
		print(f"Enriching {app["id"]} with a Credit Bureau query")
		app["bureau_score"] = 750


print("--- Examples ---")
loan_application = {
	"id": "APP-001",
	"amount": 50000,
	"term": 12
}
processor = LoanApplicationProcessor()
processor.process_application(loan_application)