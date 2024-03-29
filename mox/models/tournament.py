from enum import Enum


class Tournament:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create(attributes):
        return Tournament(
            name=attributes['name'],
            competitors=attributes['competitors']
        )

    def serialize(self):
        return {
            'name': self.name
        }
