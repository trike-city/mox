from mox import create_app, Dependencies
from config import DevelopmentConfig

config = DevelopmentConfig()
deps = Dependencies(config)
app = create_app(deps)
