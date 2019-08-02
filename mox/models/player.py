class Player:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def serialize(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname
        }
