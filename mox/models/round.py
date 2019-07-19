class Round:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def create(attributes):
        return Round(
            number=attributes['number'],
        )

    def serialize(self):
        return {
            'number': self.number
        }
