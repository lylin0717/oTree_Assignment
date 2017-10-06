from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Yulin Liu'

doc = """
Bootscats Game
"""

class Constants(BaseConstants):
    name_in_url = 'bootscats'
    players_per_group = 2
    num_rounds = 20
    start = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    cur_number = models.PositiveIntegerField(initial=1)
    is_end = models.BooleanField()
    answer = models.CharField()
    winner_id = models.PositiveIntegerField(initial=1)

    @staticmethod
    def validate(number):
        if (number % 15 == 0 or (str(3) in str(number) and str(5) in str(number))):
            return "bootscats"
        elif (number % 3 == 0 or (str(3) in str(number))):
            return "boots"
        elif (number % 5 == 0 or (str(5) in str(number))):
            return "cats"
        else:
            return str(number)

class Player(BasePlayer):
    pass
