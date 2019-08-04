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
            self.__migrations_label(migrations)
        ]
        lines = header + [m.path_str for m in migrations]
        self.out.log('\n'.join(lines))

    def __migrations_label(self, migrations):
        count = len(migrations)
        label = f'Performed {count} '

        if count == 1:
            label += 'migration:'
        else:
            label += 'migrations:'

        return label
