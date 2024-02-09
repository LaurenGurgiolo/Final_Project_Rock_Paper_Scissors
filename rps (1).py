"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.count_p1 = 0
        self.count_p2 = 0

    def move(self):
        x = random.choice(moves)
        return x

    def beats(self, one, two):
        if ((one == 'rock' and two == 'scissors') or
           (one == 'scissors' and two == 'paper') or
           (one == 'paper' and two == 'rock')):
            self.count_p1 += 1
            print("Computer Wins!")
            time.sleep(1)
        if ((one == 'scissors' and two == 'rock') or
           (one == 'paper' and two == 'scissors') or
           (one == 'rock' and two == 'paper')):
            self.count_p2 += 1
            print("Human Wins!")
            time.sleep(1)
        if ((one == 'scissors' and two == 'scissors') or
           (one == 'paper' and two == 'paper') or
           (one == 'rock' and two == 'rock')):
            print("It was a tie.")
            time.sleep(1)
        print(f"Score:\nComputer: {self.count_p1}\n"
              f"Human: {self.count_p2}")
        time.sleep(2)

    def beats_computer(self, one, two):
        if ((one == 'rock' and two == 'scissors') or
           (one == 'scissors' and two == 'paper') or
           (one == 'paper' and two == 'rock')):
            self.count_p1 += 1
            print("Computer One Wins!")
            time.sleep(1)
        if ((one == 'scissors' and two == 'rock') or
           (one == 'paper' and two == 'scissors') or
           (one == 'rock' and two == 'paper')):
            self.count_p2 += 1
            print("Computer Two Wins!")
            time.sleep(1)
        if ((one == 'scissors' and two == 'scissors') or
           (one == 'paper' and two == 'paper') or
           (one == 'rock' and two == 'rock')):
            print("It was a tie.")
            time.sleep(1)
        print(f"Score:\nComputer One: {self.count_p1}\n"
              f"Computer Two: {self.count_p2}")
        time.sleep(2)


class human_player(Player):
    def move(self):
        x = input("Rock, paper, or scissors?\n")
        if x.lower() not in moves:
            print("Invaid input, try again.")
            x = human_player.move(self)
        if x.lower() in moves:
            return x


class tactic1(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def ReflectPlayer(self):
        if self.their_move == "rock":
            move1 = "rock"
        if self.their_move == "scissors":
            move1 = "scissors"
        if self.their_move == "paper":
            move1 = "paper"
        return move1


class tactic2(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def ReflectPlayer(self):
        if self.my_move == "rock":
            move1 = "paper"
        if self.my_move == "scissors":
            move1 = "rock"
        if self.my_move == "paper":
            move1 = "scissors"
        return move1


class tactic3(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def ReflectPlayer(self):
        if self.my_move == "rock":
            move1 = "rock"
        if self.my_move == "scissors":
            move1 = "scissors"
        if self.my_move == "paper":
            move1 = "paper"
        return move1


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count_p1 = 0
        self.count_p2 = 0

    def play_round(self, round):
        if round == 0:
            move1 = self.p1.move()
            move2 = human_player.move(self)
            print(f"Computer: {move1}  Human: {move2}")
            time.sleep(1.5)
            self.count(move1, move2)
            tactic1.learn(self, move1, move2)
        if round == 1:
            move1 = tactic1.ReflectPlayer(self)
            move2 = human_player.move(self)
            print(f"Computer: {move1}  Human: {move2}")
            time.sleep(1.5)
            self.count(move1, move2)
            tactic2.learn(self, move1, move2)
        if round == 2:
            move1 = tactic2.ReflectPlayer(self)
            move2 = human_player.move(self)
            print(f"Computer: {move1}  Human: {move2}")
            time.sleep(1.5)
            self.count(move1, move2)
        if round == 3:
            move1 = self.p1.move()
            move2 = human_player.move(self)
            print(f"Computer: {move1}  Human: {move2}")
            time.sleep(1.5)
            self.count(move1, move2)
            tactic3.learn(self, move1, move2)
        if round == 4:
            move1 = tactic3.ReflectPlayer(self)
            move2 = human_player.move(self)
            print(f"Computer: {move1}  Human: {move2}")
            time.sleep(1.5)
            self.count(move1, move2)
        if round == 5:
            move1 = self.p1.move()
            move2 = human_player.move(self)
            print(f"Computer: {move1}  Human: {move2}")
            time.sleep(1.5)
            self.count(move1, move2)

    def play_computer(self, round):
        if round == 0:
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Computer One: {move1}  Computer Two: {move2}")
            time.sleep(1.5)
            self.count_computer(move1, move2)
            tactic1.learn(self, move1, move2)
        if round == 1:
            move1 = tactic1.ReflectPlayer(self)
            move2 = self.p2.move()
            print(f"Computer One: {move1}  Computer Two: {move2}")
            time.sleep(1.5)
            self.count_computer(move1, move2)
            tactic2.learn(self, move1, move2)
        if round == 2:
            move1 = tactic2.ReflectPlayer(self)
            move2 = self.p2.move()
            print(f"Computer One: {move1}  Computer Two: {move2}")
            time.sleep(1.5)
            self.count_computer(move1, move2)
        if round == 3:
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Computer One: {move1}  Computer Two: {move2}")
            time.sleep(1.5)
            self.count_computer(move1, move2)
            tactic3.learn(self, move1, move2)
        if round == 4:
            move1 = tactic3.ReflectPlayer(self)
            move2 = self.p2.move()
            print(f"Computer One: {move1}  Computer Two: {move2}")
            time.sleep(1.5)
            self.count_computer(move1, move2)
        if round == 5:
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Computer One: {move1}  Computer Two: {move2}")
            time.sleep(1.5)
            self.count_computer(move1, move2)

    def count(self, move1, move2):
        Player.beats(self, move1, move2)

    def count_computer(self, move1, move2):
        Player.beats_computer(self, move1, move2)

    def goodbye(self):
        y = input("Would you like to play again? y/n?\n")
        if "y" != y.lower() and "n" != y.lower():
            print("That is not a valid responce, try again.")
            Game.goodbye(self)
        if "y" == y.lower():
            Game.play_game(self)
        if "n" == y.lower():
            print("Goodbye")
            quit()

    def reset_count(self):
        self.count_p1 = 0
        self.count_p2 = 0

    def computervscomputer(self):
        for round in range(6):
            print(f"Round {round}:")
            time.sleep(1.5)
            self.play_computer(round)
        if self.count_p1 > self.count_p2:
            print("Computer One won the game!")
            time.sleep(1.5)
            print("Game over!")
            Game.reset_count(self)
            Game.goodbye(self)
        if self.count_p2 > self.count_p1:
            print("Computer Two won the game!")
            time.sleep(1.5)
            print("Game over!")
            Game.reset_count(self)
            Game.goodbye(self)
        if self.count_p1 == self.count_p2:
            print("The game was a tie!")
            time.sleep(1.5)
            print("Game over!")
            Game.reset_count(self)
            Game.goodbye(self)

    def computervshuman(self):
        choice = input("How many rounds would you like to play? (up to 6)\n")
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Not a valid choice, try again.")
            Game.computervshuman(self)
        if choice in ["1", "2", "3", "4", "5", "6"]:
            for round in range(int(choice)):
                print(f"Round {round}:")
                time.sleep(1.5)
                self.play_round(round)
            if self.count_p1 > self.count_p2:
                print("Computer won the game!")
                time.sleep(1.5)
                print("Game over!")
                Game.reset_count(self)
                Game.goodbye(self)
            if self.count_p2 > self.count_p1:
                print("Human won the game!")
                time.sleep(1.5)
                print("Game over!")
                Game.reset_count(self)
                Game.goodbye(self)
            if self.count_p1 == self.count_p2:
                print("The game was a tie!")
                time.sleep(1.5)
                print("Game over!")
                Game.reset_count(self)
                Game.goodbye(self)

    def computer_or_human(self):
        x = input("Human player or computer vs computer?\n"
                  "Enter (human/computer)\n")
        if "human" != x.lower() and "computer" != x.lower():
            print("Invalid input, please try again.")
            time.sleep(1)
            Game.computer_or_human(self)
        if "human" in x.lower():
            Game.computervshuman(self)
        if "computer" in x.lower():
            Game.computervscomputer(self)

    def play_game(self):
        print("Let's play some Rocks, Paper, Scissors!")
        time.sleep(1)
        print("Game start!")
        time.sleep(1)
        Game.computer_or_human(self)


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
