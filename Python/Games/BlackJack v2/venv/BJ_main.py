from BJ_art import logo
import random


print(logo)
print("Welcome in Blackjack!")

def clear():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Dealer has blackjack, you loose"
    elif user_score == 0:
        return "You've won with blackjack"
    elif user_score > 21:
        return "You went over, you loose"
    elif dealer_score > 21:
        return "Dealer went over, you won"
    elif user_score >computer_score:
        return "You've bigger score than dealer, you won"
    else:
        return "You loose"
def playgame():
    user_cards = []
    dealer_cards = []
    is_game_over = False

    for x in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Dealer cards: {dealer_cards[0]}, current score: {dealer_score}")

        if user_score == 0 or dealer_cards == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get new card, type 'n' to pass\n")
            if choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(compare(user_score,dealer_score))

while input("Do you want to play game? Type 'y' for yes and 'n' for no") == "y":
    playgame()



