from random import choice
from collections import defaultdict

from config import ALL_CARDS


class CardDealer:
    def __init__(self):
        self.cards_in_use = defaultdict(list)
        self.unused_cards = ALL_CARDS.copy()

    def generate(self, key: str, unique: bool):
        if unique:
            chosen = choice(self.unused_cards[key])
            self.cards_in_use[key].append(chosen)
            self.unused_cards[key].remove(chosen)
        else:
            chosen = choice(ALL_CARDS[key])
        return chosen

    def reset_cards(self, key: str):
        self.cards_in_use[key] = []
        self.unused_cards[key] = ALL_CARDS[key].copy()


