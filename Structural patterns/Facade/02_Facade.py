"""
Client Verification (FinTech)
Onboarding a new client involves multiple checks. A facade simplifies this operation.
"""
class KYCService:
    def verify_identity(self, tax_id: str) -> bool: 
    	print(f"KYC: Verifying...")
    	return True

class BlacklistService:
    def is_on_blacklist(self, tax_id: str) -> bool: 
    	print(f"SAT: Verifying...")
    	return False

# SRP: Its only responsibility is to orchestrate the onboarding.
# DIP: The client depends on this class, not on KYC or SAT services directly.
class ClientOnboardingFacade:
    def __init__(self): 
    	self.kyc, self.blacklist = KYCService(), BlacklistService()
    	
    def register_new_client(self, tax_id: str) -> bool:
        if self.kyc.verify_identity(tax_id) and not self.blacklist.is_on_blacklist(tax_id):
            print(f"Client {tax_id} approved and registered.")
            return True
        return False

print("--- Example ---")
onboarding = ClientOnboardingFacade()
onboarding.register_new_client("XAXX010101000")