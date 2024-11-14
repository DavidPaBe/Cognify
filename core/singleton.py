class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            # Configuración inicial
            cls._instance.config = {'simulation_speed': 'normal'}
        return cls._instance

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
