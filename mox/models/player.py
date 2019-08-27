class Player:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname
        }

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.id == other.id \
                and self.firstname == other.firstname \
                and self.lastname == other.lastname
        else:
            return False
