from artblack import logo  # Importing logo from artblack library
import random

print(logo)  # Displaying the game logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # List of card values
user_cards = []  # List to store user's cards
computer_cards = []  # List to store computer's cards

def deal_card():
    """Function to randomly select a card from the cards list"""
    return random.choice(cards)

def calculate_scores(cards_list):
    """
    Function to calculate the total score of a hand.
    Handles the Ace card value of 1 or 11 based on the total score.
    """
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0  # Blackjack
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    
    return sum(cards_list)

def play_game():
    """Function to play the game"""
    for _ in range(2):
        user_cards.append(deal_card())  # Deal 2 cards to the user
        computer_cards.append(deal_card())  # Deal 2 cards to the computer

    game_over = False
    while not game_over:
        user_score = calculate_scores(user_cards)  # Calculate user's score
        computer_score = calculate_scores(computer_cards)  # Calculate computer's score

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True  # Game ends if user wins, loses, or goes over 21
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(deal_card())  # User chooses to get another card
            else:
                print(f"Your Final hand: {user_cards}, Final Score: {user_score}")
                print(f"Computer's Final hand: {computer_cards}, Final Score: {computer_score}")
                if user_score > computer_score and user_score < 21:
                    print("Opponent went over, You Win! 😁")
                else:
                    print("You went over! Computer Wins! 🤖")
                game_over = True  # End the game

play_game()  # Start the game
