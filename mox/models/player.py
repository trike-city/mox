class Player:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @staticmethod
    def create(attributes):
        return Player(
            firstname=attributes['firstname'],
            lastname=attributes['lastname']
        )

    def serialize(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname
        }
