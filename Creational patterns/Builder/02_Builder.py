"""
Financial Report Generator (FinTech)
"""
# SRP: This class's responsibility is only to represent the report.
class FinancialReport:
	def __init__(self, title: str):
		self.title = title
		self.sections = []

	def add_section(self, content: str):
		self.sections.append(content)

	def display(self):
		print(f"Report: {self.title} "+" |".join(self.sections))


# SRP: This class's responsability is only to build the report.
class SME_ReportBuilder:
	def __init__(self, company_name: str):
		self._report = FinancialReport(f"Analysis for {company_name}")

	def add_header(self):
		self._report.add_section("HEADER")
		return self

	def get_report(self) -> FinancialReport:
		return self._report


print("--- Example ---")
builder = SME_ReportBuilder("FinTech Solutions Inc.")
report = builder.add_header().get_report()
report.display()