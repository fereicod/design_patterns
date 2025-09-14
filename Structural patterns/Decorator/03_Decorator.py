"""
Job Postings (HR Tech)
A basic job posting can be enhanced with "premium" features (decorators) that have an extra cost for X's clients.
"""
from abc import ABC, abstractmethod

# LSP: The interface that allows postings to be treated the same way.
class JobPosting(ABC):
	@abstractmethod
	def get_cost(self) -> int: pass
	@abstractmethod
	def get_features(self) -> str: pass

# OCP: The base class is CLOSED to new features.
class BasicPosting(JobPosting):
	def get_cost(self) -> int: return 500
	def get_features(self) -> str: return "Posting on X Portal"


class FeatureDecorator(JobPosting):
	def __init__(self, posting: JobPosting):
		self._posting = posting

# SRP: Its only responsability is to add the boost.
# OCP: Extended with new decorators.
class WithSocialMediaBoost(FeatureDecorator):
	def get_cost(self) -> int:
		return self._posting.get_cost() + 300

	def get_features(self) -> str:
		return self._posting.get_features() + " | Social Media"


print("--- Example ---")
premium_posting = WithSocialMediaBoost(BasicPosting())
print(f"Cost: ${premium_posting.get_cost()}, Features: {premium_posting.get_features()}")
