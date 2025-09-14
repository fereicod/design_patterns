"""
Candidate Profile Construction (HR Tech)
"""
# SRP: The class is only concreted with holding the profile data.
class CandidateProfile:
	def __init__(self, name: str):
		self.name = name
		self.experience = []

	def __str__(self):
		return f"Profile for {self.name} | Experience: {len(self.experience)} jobs"


# SRP: The class is only concreted with the logi of building the profile.
class ProfileBuilder:
	def __init__(self, name: str):
		self.profile = CandidateProfile(name)

	def with_work_experience(self, position: str, company: str):
		self.profile.experience.append({"position": position, "company": company})
		return self

	def build(self) -> CandidateProfile:
		return self.profile


print("--- Example ---")
builder = ProfileBuilder("Fernando")
profile = builder.with_work_experience("Dev", "Google").build()
print(profile)