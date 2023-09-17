from bet import Bet
from roulette import Roulette
from spin_info import SpinInfo

def main():

    game = Roulette()

    # Add an initial player, this allows for the main loop to self-terminate when there are no more players
    init_player = input("Enter player name: ")
    game.add_player(init_player)

    while len(game.players) > 0: # main loop
        print("Current players:")
        
        # list the current players and their balance
        for i in range(0, len(game.players)):
            player_name = list(game.players.keys())[i]
            player_balance = list(game.players.values())[i]
            print(f"{i + 1}.    {player_name}    £{player_balance}")

        while True: # Allow new players to join
            inp = input("Enter the names of new players (OR press ENTER if done): ")

            if inp == "":
                break

            game.add_player(inp)

        for player in game.players: # Collect the bets for each player
            print(f"{player}, please place a bet.")
            print("1. Bet on a specific number")
            print("2. Bet on an even number")
            print("3. Bet on an odd number")
            print("4. Bet on a small number (1-12)")
            print("5. Bet on a medium number (13-24)")
            print("6. Bet on a large number (25-36)")
            opt: int = int(input("Please select an option (1-6): "))

            specific: int = 0

            if opt == 1: # If a player bets on a specific number, collect that specific number
                specific = int(input("What number do you want to bet on? (1-36): "))

            amount: int = int(input("How much would you like to bet? "))

            game.bet(player, Bet(opt - 1), specific, amount)

        spin_result: SpinInfo = game.spin()

        roll: int = spin_result.result

        print(f"The roulette result was {roll}.")

        for i in range(0, len(game.players)):
            player_name = list(game.players.keys())[i]
            player_balance = list(game.players.values())[i]
            print(f"{i + 1}.    {player_name}    £{player_balance}")

        for player in game.players: # Remove any players with no money to bet
            if game.players[player] <= 0:
                game.remove_player(player)
                print(f"{player} has been forcefully removed; they have gone bankrupt.")

        if len(game.players) == 0: # end game if no players
            break

        while True: # Offer players the option to leave with their earnings, or losses
            inp = input(f"Enter what players have walked, press enter when done: ")

            if inp == "":
                break
            
            removedBalance = game.remove_player(inp)
            if removedBalance == None:
                print(f"That player doesnt exist. ({inp})")
                continue

            print(f"{inp} walked with £{removedBalance}.")
            

    print("No players left, game end.") # End game message


if __name__ == "__main__":
    main()