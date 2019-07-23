#!/usr/bin/env python3

import sys
import config

from mox.data import Database, Migrator, MigrationLogger
from pathlib import Path

if len(sys.argv) > 1:
    key = sys.argv[1]
else:
    key = None

config = config.for_key(key)

db = Database(config)
db.open()

path = Path().absolute() / 'mox/data/migrations'

migrator = Migrator(db, path)
migrations = migrator.migrate_latest()

logger = MigrationLogger(config)
logger.log_performed_migrations(migrations)

db.close()
