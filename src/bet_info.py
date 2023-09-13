from bet import Bet

class BetInfo:
    def __init__(self, player: str, bet: Bet, specific: int, amount: int) -> None:
        self.player = player
        self.bet = bet
        self.specific = specific
        self.amount = amount