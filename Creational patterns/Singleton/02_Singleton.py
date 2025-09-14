"""
API Configuration Manager (FinTech)
"""
class ApiConfigManager:
    _instance, _config = None, None
    
    def __new__(cls):
        if not cls._instance: cls._instance = super().__new__(cls)
        return cls._instance
    
    # SRP (partial): The class handles its own creation and manages configuration.
    # This can be a violation if the configuration logic grows too large.
    def get_config(self, key: str):
        if self._config is None:
            print("Loading API config... (ONLY HAPPENS ONCE)")
            self._config = {"BUREAU_API_KEY": "SECRET_KEY_123"}
        return self._config.get(key)

print("--- Example ---")
config1 = ApiConfigManager()
config2 = ApiConfigManager()
print(f"Are they the same instance?: {config1 is config2}")