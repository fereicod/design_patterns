"""
Database Connection (HR Tech)
"""
import time

class DBPoolManager:
    _instance = None
    _connection_pool = None

    # The Singleton controls its own creation, encapsulating this logic.
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    # DIP (Warning): Other modules using DBPoolManager() directly
    # will create a strong coupling to this concrete class, which can
    # hinder testing and flexibility (a DIP violation).
    def get_connection(self) -> str:
        if self._connection_pool is None:
            print("Creating database connection pool... (this is slow and should only happen once)")
            time.sleep(1) # Simulate latency
            self._connection_pool = ["conn1", "conn2"]
        return self._connection_pool[0]

# --- Usage ---
print("--- Example ---")
db_manager1 = DBPoolManager()
db_manager1.get_connection()

print("The second access does not re-create the pool:")
db_manager2 = DBPoolManager()
db_manager2.get_connection()
print(f"Are they the same instance?: {db_manager1 is db_manager2}")