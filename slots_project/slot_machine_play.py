import random

class SlotMachine:
    def __init__(self):
        self.icons = ['🍒', '🍊', '🍋', '🍉', '🍇', '🍓', '🍀']
        self.bet = 0
        self.balance = 0

    def play(self):
        if self.balance <= 0:
            print("Sorry, you ran out of money. Goodbye!")
            return

        while True:
            try:
                self.bet = int(input("\nWhat is your bet?"))
                if self.bet <= 0 or self.bet > self.balance:
                    raise ValueError
                break
            except ValueError:
                print(f"Invalid bet. Please enter a number between 1 and {self.balance}")

        reels = [random.choice(self.icons) for i in range(3)]
        print()
        print(" ".join(reels))

        if '🍋' in reels:
            print("You squeezed the lemon and there is no win for you! Sorry...")
            return
        elif '🍀' in reels:
            winnings = self.bet * 3
            print("Lucky you! You trippled your bet! Let the other players envy you!\n'-'*2")
        elif reels[0] == reels[1] == reels[2]:

            if reels[0] == reels[1] == reels[2] == '🍀':
                winnings = self.bet * 20
                print(f"SUPERB JACKPOT!!! You won BGN {winnings}!")
            winnings = self.bet * 10
            print(f"JACKPOT!!! You won BGN {winnings}!")

        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            winnings = self.bet * 2
            print(f"You won BGN {winnings}! Give it a next try for a BIGGER win!\n---------------------------------------------------")

        else:
            winnings = 0
            print("Sorry, no winning...")

        self.balance += winnings - self.bet
        print(f"Your balance is now BGN {self.balance}\n---------------------------------------------------")

    def add_money(self, amount):
        self.balance += amount
        print(f"Added BGN{amount} to your balance. \nYour new balance is BGN{self.balance}.")

    def remove_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"BGN{amount} was removed from your balance. Your new balance is: BGN{self.balance}.")
