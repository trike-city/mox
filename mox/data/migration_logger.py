class Console:
    def log(self, output):
        print(output)


class MigrationLogger:
    def __init__(self, config, out=Console()):
        self.out = out
        self.config = config

    def log_performed_migrations(self, migrations):
        header = [
            f'Environment: {self.config.name}',
            f'Performed {len(migrations)} migrations:'
        ]
        lines = header + [m.path_str for m in migrations]
        self.out.log('\n'.join(lines))
