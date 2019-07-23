#!/usr/bin/env python3

import sys
import config

from mox.data import Database, Migrator, MigrationLogger


if len(sys.argv) > 1:
    key = sys.argv[1]
else:
    key = None

config = config.for_key(key)

db = Database(config)
migrator = Migrator(db)
logger = MigrationLogger(config)

db.open()

migrations = migrator.migrate_latest()
logger.log_performed_migrations(migrations)

db.close()
