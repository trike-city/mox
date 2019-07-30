from mox import create_app
from config import DevelopmentConfig


config = DevelopmentConfig()
app = create_app(config)
