from card_dealer import CardDealer
from config import PLAYER_PROFILE_KEYS, \
    ACTIONCARDS_KEY, \
    CATASTROPHE_KEY, \
    BUNKER_PROFILE_KEYS


class GameManager:
    def __init__(self, usernames: list):
        self.card_dealer = CardDealer()
        self.catastrophe_card = self.generate_catastrophe()
        self.bunker = Bunker()
        self.players = {username: Player(username, self.card_dealer) for username in usernames}

    def regenerate_players(self, key: str):
        self.card_dealer.reset_cards(key)
        [
            player.regenerate(key)
            for player in self.players.values()
        ]

    def generate_catastrophe(self):
        return self.card_dealer.generate(CATASTROPHE_KEY, unique=False)

    def regenerate_catastrophe(self):
        self.catastrophe_card = self.generate_catastrophe()


class Bunker:
    def __init__(self):
        pass

    def generate(self, key: str, unique: bool):
        assert key in BUNKER_PROFILE_KEYS, "class Bunker is not responsible for generating non-bunker cards"


class Player:
    def __init__(self, username: str, card_dealer: CardDealer):
        self.username = username
        self.card_dealer = card_dealer
        self.profile = {
            profile_card_name: self.generate(profile_card_name)
            for profile_card_name in PLAYER_PROFILE_KEYS
        }
        self.actioncard_1_card = self.generate_actioncard()
        self.actioncard_2_card = self.generate_actioncard()

    def generate(self, key: str, unique: bool=False):
        assert key in PLAYER_PROFILE_KEYS, "class Player is not responsible for generating non-player cards"
        return self.card_dealer.generate(key, unique=unique)

    def regenerate(self, key: str):
        self.profile[key] = self.generate(key)

    def generate_actioncard(self, unique: bool=True):
        return self.card_dealer.generate(ACTIONCARDS_KEY, unique=unique)

    def regenerate_actioncards(self):
        self.actioncard_1_card = self.generate_actioncard()
        self.actioncard_2_card = self.generate_actioncard()


print("asdads")