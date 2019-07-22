#!/usr/bin/env python3

from mox.data import Database, Migrator
from config import DevelopmentConfig
from pathlib import Path


config = DevelopmentConfig()
db = Database(config)

db.open()

path = Path().absolute() / 'mox/data/migrations'
migrator = Migrator(db, path)
migrator.migrate_latest()

db.close()
