# stlib
from random import randint

from bet_info import BetInfo
from spin_info import SpinInfo
from bet import Bet
import rules

class Roulette:
    def __init__(self) -> None:
        self.bets = dict()
        self.players = dict()
        self.spin_history = list() # technically redundant, but just in case

    def add_player(self, player: str) -> None:
        self.players[player] = rules.START_BALANCE

    def remove_player(self, player: str) -> int:
        if player in self.players:
            return self.players.pop(player) # remove player and return balance
        return None # player cannot be removed, as player does not exist

    def bet(self, player: str, bet: Bet, specific: int, amount: int) -> bool:
        if player not in self.players:
            return False # player not in the game

        self.bets[player] = BetInfo(player, bet, specific, amount)

        return True

    # INTERNAL MEMBER FUNCTION
    def __spin(self) -> int:
        return randint(1, 36)
        
    # INTERNAL MEMBER FUNCTION
    def __apply_spin(self, spin: int) -> None:
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
                case Bet.MEDIUM:
                    if spin >= 13 and spin <= 24:
                        self.players[player] += bet_info.amount * rules.MEDIUM_MULT
                case Bet.LARGE:
                    if spin >= 25 and spin <= 36:
                        self.players[player] += bet_info.amount * rules.LARGE_MULT

    def spin(self) -> SpinInfo:
        spin_result = self.__spin()
        self.__apply_spin(spin_result)

        # an info object for displaying values
        spin_info = SpinInfo(spin_result, self.bets)
        self.spin_history.append(spin_info)

        # clear bets for next spin
        self.bets = dict()

        return spin_info
