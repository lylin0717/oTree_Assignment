from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Player1(Page):
    form_model = models.Group
    form_fields = ['answer']

    def is_displayed(self):
        group = self.group
        group.is_end = self.group.in_round(self.round_number - 1).is_end if self.round_number > 1 else True
        prev_number = self.group.in_round(self.round_number - 1).cur_number if self.round_number > 1 else 1
        group.cur_number = prev_number if self.round_number > 1 else prev_number
        return self.player.id_in_group == 1 and self.group.is_end

    def before_next_page(self):
        group = self.group
        if (group.answer == group.validate(group.cur_number)):
            print("Player 1 entered correct number")
            group.cur_number += 1
        else:
            group.is_end = False
            group.winner_id = 2
            print("Player 1 entered wrong")

class WaitForPlayer1(WaitPage):
    pass

class Player2(Page):
    form_model = models.Group
    form_fields = ['answer']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.is_end

    def before_next_page(self):
        group = self.group

        if (group.answer == group.validate(group.cur_number)):
            print("Player 2 entered correct number")
            group.cur_number += 1
        else:
            group.is_end = False
            group.winner_id = 1
            print("Player 2 entered wrong")

class WaitForPlayer2(WaitPage):
    pass

class Results(Page):
    def is_displayed(self):
        return not self.group.is_end

page_sequence = [
    Introduction,
    Player1,
    WaitForPlayer1,
    Player2,
    WaitForPlayer2,
    Results
]
