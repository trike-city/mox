class Migration:
    def __init__(self, path):
        self.path = path

    @property
    def name(self):
        file_name = str(self.path).split('/')[-1]
        return file_name.split('.')[0]

    def up(self, database):
        scope = {}
        content = self.path.read_text()
        exec(content, scope)
        scope['up'](database)
