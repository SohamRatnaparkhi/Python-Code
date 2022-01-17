import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank) :

        self.rank = rank
        self.suit = suit
        Card.values = values[rank]

    def __str__(self):
        return self.rank + 'of' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                deck_card = Card(suit, rank)
                self.all_cards.append(deck_card)

    def shuffle(self):
        random.shuffle(self.all_cards)
        self.shuffle_list = self.all_cards

        return self.shuffle_list

    def remove_one_card(self):
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

new_deck = Deck
new_deck = Deck.shuffle()

player_1 = Player("One")
player_2 = Player("Two")

count = 1

for card in new_deck:
    if count <= 26:
        player_1.all_cards.append(card)
    else:
        player_2.all_cards.append(card)

game_on = True
while game_on:
    if len(player_1.all_cards)  == 0:
        game_on = False
        print ("Player 2 WON the game")
        break
    elif len(player_2.all_cards) == 0:
        game_on = False
        print ("Player 1 WON the game")
        break
    else:
        game_on = True
        
