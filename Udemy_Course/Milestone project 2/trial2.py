import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
                 
playing = True

class Card:
    #Class to create a card    
    def __init__(self, suit, rank):
        """Create a card.

        Args:
            suit ([str]): [Can be Heart or a spade or a Diamond or Club]
            rank ([str]): [rank of rach card]
        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.value + ' of ' + self.suit

class Deck:
    """ Store 52 card objects in a list that can later be shuffled with the help of function shuffle_deck. 
        First, though, we need to *instantiate* all 52 unique card objects and add them to our list. 
    """
    def __init__(self):
        self.deck = []
        """Creates a deck of cards
        """
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle_deck(self):
        """Shuffles the deck
        """
        random.shuffle(self.deck)
        #return self.deck

    def deal_one(self):
        """Deals one card
        """
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.ace = 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    #chips = Chips()
    chips.bet = 0
    while chips.total < chips.bet:
        print(f"Money left in your account is {chips.total}")
        try:
            chips.bet = input("Enter money upon which you want to bet. (bet should be less than available money):-")
        except:
            print("Please enter a number!")

def hit(deck,hand):
    hand.add_card(deck.deal_one)
    hand.adjust_for_ace()
    pass

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    choice = input("Enter Hit or Stand: ")
    choice_u = choice.upper()
    if choice_u == "HIT"  or choice_u == 'H':
        hit(deck, hand)
    else:
        print("Player stands! Dealer's turn.")
        playing = False
        
def show_some(player,dealer):
    print("Dealer's hand!")
    print("Dealer has his one card hidden")
    print(f"{dealer.cards[1]}")

    print("\n Player's hand!")
    for card in player.cards:
        print(card)
    pass
    
def show_all(player,dealer):
    print("\nDealer's hand!")
    for card in dealer.cards:
        print(card)

    print(f"Value of Dealer's card is {dealer.value}")

    print("\n Player's hand!")
    for card in player.cards:
        print(card)

    print(f"Value of Player's card is {player.value}")
    pass

def player_busts(player, dealer, chips):
    print("Player BUSTS!")
    chips.lose_bet   
    pass

def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet  

def dealer_busts(player, dealer, chips):
    print("Dealer BUSTS!")
    chips.win_bet   
    pass

def dealer_wins(player, dealer, chips):
    print("Dealer WINS!")
    chips.lose_bet   

def push(player, dealer):
    print("Player and Dealer tie! PUSH")
      
while True:
    # Print an opening statement
    print("Welcome to BlackJack")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle_deck()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_one)
    player_hand.add_card(deck.deal_one)
    dealer_hand.add_card(deck.deal_one)
    dealer_hand.add_card(deck.deal_one)

    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
    
        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    
    # Inform Player of their chips total 
    print(f"\nAmount left with the player is {player_chips.total}")
    # Ask to play again
    replay = input("Would you like to play again, Yes or No (y/n) :- ")
    result = replay.lower()

    if result == y:
        playing = True
        continue
    else:
        print("Thank you for playing!")
        playing = False
        break
