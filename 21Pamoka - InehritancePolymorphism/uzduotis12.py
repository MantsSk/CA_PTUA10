import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class GameController:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]

    def roll_dice(self):
        return random.randint(1, 6)

    def play_game(self):
        print("Welcome to the Dice Rolling Game!")

        while True:
            actual_roll = self.roll_dice()
            print(f"\nNew round! The die has been rolled.")

            for player in self.players:
                guess = int(input(f"{player.name}, make your guess (1-6): "))
                print(f"{player.name} guessed {guess}.")

                if 1 <= guess <= 6:
                    if guess == actual_roll:
                        player.score += 2  # Award extra points for an exact match.
                        print(f"Correct guess! {player.name} earns 2 points.")
                    elif abs(guess - actual_roll) == 1:
                        player.score += 1  # Award 1 point for a close guess.
                        print(f"Close enough! {player.name} earns 1 point.")
                    else:
                        print(f"Sorry, incorrect guess for {player.name}.")
                else:
                    print(f"Invalid guess for {player.name}. Please enter a number between 1 and 6.")

            print("\nRound results:")
            for player in self.players:
                print(f"{player.name}'s score: {player.score}")

            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing! Game over.")
                break

player_names = input("Enter player names (comma-separated): ").split(',')
game_controller = GameController(player_names)
game_controller.play_game()
