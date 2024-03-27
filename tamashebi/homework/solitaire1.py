import random

# Function to create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Function to display the game board
def display_board(deck, tableau, foundations):
    print("\nFoundations:")
    for suit, cards in foundations.items():
        print(f"{suit}: {' '.join(card['rank'] for card in cards)}")

    print("\nTableau:")
    for pile_num, pile in enumerate(tableau):
        print(f"{pile_num+1}: {' '.join(card['rank'] for card in pile) if pile else '<empty>'}")

    print("\nStock:")
    print(f"Remaining cards: {len(deck)}")

# Function to deal cards from the deck to the tableau
def deal_cards(deck):
    tableau = [[] for _ in range(7)]
    for i in range(7):
        for j in range(i, 7):
            tableau[j].append(deck.pop(0))
            if j == i:
                tableau[j][-1]['hidden'] = False
    return tableau

# Function to check if the game is won
def check_win(foundations):
    return all(len(cards) == 13 for cards in foundations.values())

# Function to play the game
def play_solitaire():
    deck = create_deck()
    tableau = deal_cards(deck)
    foundations = {'Hearts': [], 'Diamonds': [], 'Clubs': [], 'Spades': []}

    while not check_win(foundations):
        display_board(deck, tableau, foundations)
        move = input("Enter your move (e.g., 'T2 F') or 'D' to draw a card: ").strip().upper()

        if move == 'D':
            if deck:
                card = deck.pop(0)
                card['hidden'] = False
                tableau[0].append(card)
            else:
                print("No cards remaining in the deck!")
        elif move[0] == 'T' and move[1:].isdigit():
            from_pile = int(move[1:]) - 1
            to_pile = input("Enter destination foundation (e.g., 'F'): ").strip().upper()
            if to_pile in foundations:
                if tableau[from_pile]:
                    card = tableau[from_pile].pop()
                    foundations[to_pile].append(card)
                else:
                    print("Source tableau pile is empty!")
            else:
                print("Invalid destination foundation!")
        else:
            print("Invalid move!")

    print("Congratulations! You won!")

# Start the game
play_solitaire()












































































































































































