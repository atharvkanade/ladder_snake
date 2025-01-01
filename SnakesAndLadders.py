import random


class SnakesAndLadders:
    def __init__(self):
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53,
                       62: 19, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {2: 38, 7: 14, 8: 31, 15: 26,
                        21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98}
        self.player_position = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self):
        dice = self.roll_dice()
        
        print(f"You rolled a {dice}.")
        self.player_position += dice

        if self.player_position > 100:
            self.player_position -= dice
            print("You need an exact roll to win! Stay at the same position.")

        if self.player_position in self.snakes:
            print(
                f"Oops! You landed on a snake. Go down to {self.snakes[self.player_position]}.")
            self.player_position = self.snakes[self.player_position]
        elif self.player_position in self.ladders:
            print(
                f"Yay! You climbed a ladder. Go up to {self.ladders[self.player_position]}.")
            self.player_position = self.ladders[self.player_position]

        print(f"Your current position is {self.player_position}.\n")

    def play_game(self):
        print("Welcome to Snakes and Ladders!")
        print("Reach position 100 to win the game.")

        while self.player_position < 100:
            input("Press Enter to roll the dice...")
            self.move_player()

        print("Congratulations! You reached position 100 and won the game!")


game = SnakesAndLadders()
game.play_game()
