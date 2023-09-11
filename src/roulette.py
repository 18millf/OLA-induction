# stlib
from random import range

from bet_info import BetInfo
from bet import Bet
import rules

class Roulette:
    def __init__(self, players) -> None:
        self.bets = {}
        self.players = {}
        
        for player in players:
            self.players[player] = rules.START_BALANCE # players dictionary has the players name and balance

    def bet(self, player: str, bet: Bet, specific: int, amount: int) -> bool:
        if player not in self.players:
            return False # player not in the game

        self.bets[player] = BetInfo(bet, specific, amount)

        return True

    def _spin(self) -> int:
        return range(1, 36)
        
    def apply_spin(self, spin: int):
        for player in self.players:
            bet_info = self.bets[player]

            self.players[player] -= bet_info.amount

            match bet_info.bet:
                case Bet.SPECIFIC:
                    if bet_info.specific == spin:
                        self.players[player] += bet_info.amount * rules.SPECIFIC_MULT
                case Bet.EVEN:
                    if spin % 2 == 0:
                        self.players[player] += bet_info.amount * rules.EVEN_MULT
                case Bet.ODD:
                    if spin % 2 != 0:
                        self.players[player] += bet_info.amount * rules.ODD_MULT
                case Bet.SMALL:
                    if spin >= 1 and spin <= 12:
                        self.players[player] += bet_info.amount * rules.SMALL_MULT

                # TODO: stuff for MEDIUM and LARGE


