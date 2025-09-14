"""
Candidate Hiring (HR Tech)
The process to "hire" a candidate is complex. A facade simplifies it to a single method call.
"""
class ATSSystem:
    def update_status(self, c_id: int, status: str): 
    	print(f"ATS: Updating candidate {c_id} status to '{status}'.")

class ContractGenerator:
    def generate(self, name: str, position: str) -> str: 
    	print(f"Contracts: Generating contract for {name} as {position}.")
    	return "c.pdf"

# SRP: The facade's unique responsibility is to orchestrate the hiring.
# DIP: The high-level module that hires depends on this facade, not the subsystems.
class HiringFacade:
    def __init__(self):
        self.ats = ATSSystem()
        self.contracts = ContractGenerator()

    def hire_candidate(self, candidate: dict):
        print(f"Starting hiring process for {candidate['name']}...")
        self.ats.update_status(candidate['id'], "Hired")
        self.contracts.generate(candidate['name'], candidate['position'])
        print("Hiring process finished.")


print("--- Example ---")
candidate_to_hire = {"id": 101, "name": "Elena", "position": "Product Manager"}
hiring_process = HiringFacade()
hiring_process.hire_candidate(candidate_to_hire)