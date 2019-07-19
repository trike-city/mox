from enum import Enum


class Tournament:
    def __init__(self, name, competitors):
        self.name = name
        self.competitors = competitors

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
