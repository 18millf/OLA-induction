from bet import Bet

class BetInfo:
    def __init__(self, bet: Bet, specific: int, amount: int) -> None:
        self.bet = bet
        self.specific = specific
        self.amount = amount