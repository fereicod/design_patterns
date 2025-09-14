"""
Candidate Matching (HR Tech)
Could use different algorithms (strategies) to "match" a candidate to a job opening: by keywords, experience, or an AI model.
"""
from abc import ABC, abstractmethod

# DIP: The matching strategy abstraction.
class MatchingStrategy(ABC):
	@abstractmethod
	def calculate_match(self, candidate: dict, job: dict) -> int: pass

# SRP: It's only responsability is to match by keywords.
class KeywordMatchingStrategy(MatchingStrategy):
	def calculate_match(selfn, candidate: dict, job: dict) -> int:
		print("Calculating match by Keywords...")
		candidate_skills = set(candidate["skills"])
		job_skills = set(job["required_skills"])
		matches = candidate_skills.intersection(job_skills)
		return int((len(matches) / len(job_skills) * 100))

# OCP: This class is CLOSED for modification when new strategies are added,
class TalentFinder:
	# DIP: It depends on the abstraction, not a concrete matching type.
	def __init__(self, strategy: MatchingStrategy):
		self._strategy = strategy

	def find_best_candidate(self, candidate: list, job: dict):
		for candidate in candidates:
			score = self._strategy.calculate_match(candidate, job)
			print(f"The {candidate["name"]} candidate have {score} in {job["id"]}")

print("--- Example ---")
candidates = [
	{
		"name": "Fernaando",
		"skills": [
			"python",
			"django",
			"fastapi"
		],
		"experience_years": 4
	},
	{
		"name": "Jorge",
		"skills": [
			"python",
			"javascript",
		],
		"experience_years": 6
	}
]
job = {
	"id": "JOB-001",
	"required_skills": [
		"python",
		"django",
		"fastapi"
		"aws",
	],
	"min_experience": 2
}
finder = TalentFinder(KeywordMatchingStrategy())
finder.find_best_candidate(candidates, job)
