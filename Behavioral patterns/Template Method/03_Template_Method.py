"""
Candidate Evaluation Pipeline (HR Tech)
The process for evaluating candidates follows a general pipeline, but the specific screening and assessment steps change per job opening.
"""
from abc import ABC, abstractmethod

class EvaluationPipeline(ABC):
	# OCP: This template method defines the standard evaluation pipeline and is CLOSED for modification.
	def run_pipeline(self, candidate: dict):
		print(f"Starting evaluation for {candidate["name"]} for the {candidate["position"]} position...")
		# DIP: This high-level pipeline depends on abstractions implemented by subclasses.
		if self.automatic_cv_screening(candidate):
			self.perform_technical_assessment(candidate)
			self.schedule_hr_interview(candidate)
			print(f"Initial evaluation phase completed for {candidate["name"]}.")
		else:
			print(f"Candidate {candidate["name"]} did not pass automatic screening.")

	def schedule_hr_interview(self, candidate: dict):
		print(f"Schedule HR interview for {candidate["name"]}.")


	# OCP: The system is OPEN for extension through these implementations for differents roles.
	@abstractmethod
	def automatic_cv_screening(self, candidate: dict) -> bool: pass
	@abstractmethod
	def perform_technical_assessment(self, candidate: dict): pass


# Specific pipeline for a Python Backend developer role (the extension)
class PythonDevEvaluationPipeline(EvaluationPipeline):
	def automatic_cv_screening(self, candidate: dict) -> bool:
		print("Screening CV for keywords: Python, Django, FastAPI, SQL")
		return "python" in candidate["skills"] and "sql" in candidate["skills"]

	def perform_technical_assessment(self, candidate: dict):
		print(f"Sendind a Python and Algorithms technical assessment to {candidate["name"]}.")

print("--- Example ---")
backend_candidate = {
	"name": "Fernando",
	"position": "Python Backend Developer",
	"skills": [
		"python",
		"django",
		"fastapi",
		"sql",
		"docker"
	]
}
python_pipeline = PythonDevEvaluationPipeline()
python_pipeline.run_pipeline(backend_candidate)