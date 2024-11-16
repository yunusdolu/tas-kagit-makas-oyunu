
import random
from abc import ABC, abstractmethod

# Abstract base class for a player
class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.move_history = []

    @abstractmethod
    def make_move(self):
        pass

# Concrete class for a human player
class HumanPlayer(Player):
    def make_move(self):
        move = input(f"{self.name}, lütfen hamlenizi girin (taş, kağıt, makas): ").lower()
        while move not in ['Taş', 'Kağıt', 'Makas']:
            print("Geçersiz hamle. Lütfen taş, kağıt veya makas girin.")
            move = input("Hareketinizi girin:").lower()
        self.move_history.append(move)
        return move

# Abstract class for a computer player
class ComputerPlayer(Player, ABC):
    @abstractmethod
    def make_move(self):
        pass

# Concrete class for a random-move computer player
class RandomComputerPlayer(ComputerPlayer):
    def make_move(self):
        move = random.choice(['Taş', 'Kağıt', 'Makas'])
        self.move_history.append(move)
        print(f"Bilgisayar seçti{move}.")
        return move

# Function to determine the result of the game
def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif (player_move == "Taş" and computer_move == "Makas") or          (player_move == "Makas" and computer_move == "Kağıt") or          (player_move == "Kağıt" and computer_move == "Taş"):
        return "Oyuncu"
    else:
        return "Bilgisayar"

# Function to display the score
def display_score(player, computer):
    print(f"Skor - {player.name}: {player.score}, CoBilgisayarmputer: {computer.score}")

# Main game function
def play_game():
    player_name = input("Adınızı girin: ")
    player = HumanPlayer(player_name)
    computer = RandomComputerPlayer("Bilgisayar")

    while True:
        print("\n--- Yeni Tur ---")
        player_move = player.make_move()
        computer_move = computer.make_move()

        result = determine_winner(player_move, computer_move)

        if result == "Oyuncu":
            print(f"{player.name} bu turu kazandı!")
            player.score += 1
        elif result == "computer":
            print("Bilgisayar bu turu kazandı!")
            computer.score += 1
        else:
            print("Bu bir kravat!")

        display_score(player, computer)

        continue_game = input("Bir tur daha oynamak ister misin? (evet/hayır): ").lower()
        if continue_game != "Evet":
            break

    # Display final scores and move history
    print("\nOyunu Bitti")
    display_score(player, computer)
    print(f"\nŞunun için Geçmişi Taşı {player.name}: {player.move_history}")
    print(f"Bilgisayar için Taşıma Geçmişi: {computer.move_history}")

if __name__ == "__main__":
    play_game()
