"""
Application Status Change (HR Tech)
"""
from abc import ABC, abstractmethod

# DIP: Key abstractions.
class Observer(ABC):
	@abstractmethod
	def update(self, subject): pass

class Subject(ABC):
	@abstractmethod
	def register_observer(self, observer: Observer): pass
	@abstractmethod
	def notify_observers(self): pass

# OCP: The class doesn't need to change to add new notifiers, CLOSED.
class CandidateApplication(Subject):
	_observers: list[Observer] = []
	_status: str = ""

	# DIP: The register_observer method depends on the Observer abstraction
	def register_observer(self, observer: Observer):
		self._observers.append(observer)

	def notify_observers(self):
		for observer in self._observers:
			observer.update(self)

	def change_status(self, new_status: str):
		self._status = new_status
		self.notify_observers()


# OCP: New observers can be created without changin the subject.
class MetricsDashboard(Observer):
	def update(self, subject: CandidateApplication):
		print(f"-> Dashboard: Logging metric: 1 candidate moved to status '{subject._status}'")


print("--- Example ---")
app = CandidateApplication()
app.register_observer(MetricsDashboard())
app.change_status("Offer Made")