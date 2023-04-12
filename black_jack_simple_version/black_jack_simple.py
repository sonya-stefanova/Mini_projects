import random
from black_jack_art import logo

# First, creating the functions that will be implemented.

def random_card_generator():
    """Returns a random card from the deck."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(deck)
    return random_card


def calculate_scores(deck):
    """Return the score calculated from the deck. 
    But first check for a BlackJack or replacing the Ace with 1."""
    sum_deck = sum(deck)
    num_cards = len(deck)
    
    if sum_deck == 21 and num_cards == 2:
        return 0

    if 11 in deck and sum_deck > 21:
        deck.remove(11)
        deck.append(1)

    return sum_deck


def winner_definition(player_score, pc_score):
    """Figuring out who is the winner by comparing the scores."""
    if player_score > 21 and pc_score > 21:
        return "😤 Over 21. Unfertunately, you lose 😤"

    #firstly, we are checking for the cases that are exclusions so they might not be missed out"
    if player_score == pc_score:
        return "🙃 Draw 🙃"
    elif pc_score == 0:
        return "😱 Cry baby, Cry ==> You lose ==> Your virtual friend has BlackJack 😱"
    elif player_score == 0:
        return "😎 Luck You 😎 <==> 😎 YOU WIN with a BlackJack 😎"
    elif player_score > 21:
        return "😭 OH NO! You lose [Over 21] 😭"
    elif pc_score > 21:
        return "Lucky You! YOU WIN cause your opponent lose. 😁"
    elif player_score > pc_score:
        return "🥳😃🥳 Yeaaah! You WIN 🥳😃🥳\n\n"
    else:
        return "😤 Pfff, You LOSE 😤"

def play_game():
    print(logo)

    # Dealing the cards for each of the participants
    user_deck = []
    computer_deck = []
    is_game_over = False

    for _ in range(2):
        user_deck.append(random_card_generator())
        computer_deck.append(random_card_generator())

    while not is_game_over:
        # Game is over if the computer or the user has a blackjack (0) or if the user's score is over 21.
        player_score = calculate_scores(user_deck)
        pc_score = calculate_scores(computer_deck)
        print(f"===> Your hand is: {user_deck} with current score: {player_score}")
        print(f"===> Computer's card is: {computer_deck[0]}")

        #when the game is over and you leave the while loop:
        if player_score == 0 or pc_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_get_another_random_card = input("Type 'y' to get another random_card, type 'n' to pass: ")
            if user_get_another_random_card == "y":
                user_deck.append(random_card_generator())
            else:
                is_game_over = True

    # The computer should keep drawing deck as long as it has a score less than 17.
    while pc_score != 0 and pc_score < 17:
        computer_deck.append(random_card_generator())
        pc_score = calculate_scores(computer_deck)

    print(f"===> Your final hand: {user_deck}, final score: {player_score}")
    print(f"===> Computer's final hand: {computer_deck}, final score: {pc_score}")
    print(winner_definition(player_score, pc_score))

while input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
else:
    print("BYE BYE")
