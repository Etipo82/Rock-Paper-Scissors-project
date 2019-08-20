import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        my_move = their_move
        their_move = my_move


class RandomPlayer(Player):
    def move(self):
        shoot = random.choice(moves)
        return shoot


class ReflectPlayer(Player):
    def __init__(self):
        self.score = 0

    def move(self):
        shoot = moves
        if shoot == "rock":
            return "rock"
        elif shoot == "paper":
            return "paper"
        elif shoot == "scissors":
            return "scissors"
        else:
            return "rock"


class CyclePlayer(Player):
    def __init__(self):
        self.score = 0

    def move(self):
        shoot = moves
        if shoot == "rock":
            return "paper"
        if shoot == "paper":
            return "scissors"
        if shoot == "scissors":
            return "rock"
        else:
            return "rock"


class HumanPlayer(Player):
    def move(self):
        shoot = input(f"Rock Paper, Scissors, say shoot! Select {moves} :\n")
        while shoot != 'rock' and shoot != 'paper' and shoot != 'scissors':
            print(f"Unknown input. Please Select from, {moves}")
            shoot = input("rock, paper, scissors? >")
        return(shoot)


class Game():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        total = 0
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.score(move1, move2)
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if result == move1:
            self.p1.score += 1
            print("User One wins!")
        elif result == move2:
            self.p2.score += 1
            print("Victory for the CPU!")
        else:
            print("Tie game!")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print("PLAYER ONE TAKES THE CAKE!")
        elif self.p1.score < self.p2.score:
            print("PLAYER TWO TAKES THE CAKE!")
        else:
            print("The game was a tie!")
        play_again = input("Press: 1 to play again\n"
                           "Press: Any Key to quit\n")
        while play_again == "1":
            game.play_game()
        else:
            print("Thanks for Playing")
            quit()

    def play(self, move1, move2):
        print(f"You played {move1}")
        print(f"Opponent played {move2}")
        if Game.beats(move1, move2):
            print("Player One Wins")
            print(f"score: Player 1: {move1}  Player 2: {move2}\n\n")
            self.p1.score += 1
            return 1
        elif Game.beats(move2, move1):
            print("Player Two Wins")
            print(f"score: Player 1: {move1}  Player 2: {move2}\n\n")
            self.p2.score += 1
            return 2
        else:
            print("TIE GAME")
            print(f"Score: Player 1: {move1}  Player 2: {move2}\n\n")
            return 0

    def beats(move1, move2):
        if (move1 == 'rock' and move2 == 'scissors'):
            return True
        elif (move1 == 'scissors' and move2 == 'paper'):
            return True
        elif (move1 == 'paper' and move2 == 'rock'):
            return True
        return False

    def score(move1, move2):
        if Game.beats(move1, move2):
            return move1
        elif Game.beats(move2, move1):
            return move2
        else:
            return 0


if __name__ == '__main__':
    strategies = {
    "1": Player(),
    "2": RandomPlayer(),
    "3": CyclePlayer(),
    "4": ReflectPlayer()
    }

    user_input = input("Select the player strategy\n "
                       "you want to play against\n"
                       "1- Rock Player\n"
                       "2- Random Player\n"
                       "3- Cycle Player\n"
                       "4- Reflect Player\n")

    game = Game(HumanPlayer(), strategies[user_input])
    game.play_game()
