suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __repr__(self):
        return self.rank + " of " + self.suit

    def get_value(self):
        return self.value
    def change_ace_value(self):
        if self.rank == "Ace":
            self.value = 1
    

class Deck:
    # upon calling for a deck, an array is created using two loops to create multiple cards
    # then shuffled
    # added a shuffle method
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    
    def __repr__(self):
        deck_list = """"""
        for card in self.deck:
            deck_list += card.rank + " of " + card.suit
            deck_list += "\n"
        return deck_list

    def shuffle_deck(self):
        import random
        random.shuffle(self.deck)
    
    def deal_card(self):
        card = self.deck.pop()
        
        return card
    
class Hand():
    def __init__(self):
        self.cards = []
        self.score = 0
        self.has_ace = 0

    
    def add_card(self, card):
        self.cards.append(card)
        self.score += values[card.rank]
        if card.rank == "Ace":
            self.has_ace += 1
        
    def adjust_for_ace(self):
        while self.score > 21 and self.has_ace:
            self.score -= 10
            self.has_ace -= 1

    def get_score(self):
        self.adjust_for_ace()
        return self.score
    
    def __repr__(self):
        the_hand = ""
        if len(self.cards) > 0:
            the_hand += "There" + (" are " if len(self.cards) > 1 else " is ") + str(len(self.cards)) + " card" + ("s " if len(self.cards) > 1 else " ") + "in your hand."
            for card in self.cards:
                the_hand += "\n"
                the_hand += card.rank + " of " + card.suit
        else:
            the_hand = "There are no cards in your hand."
        return the_hand

class Player():
    pass

class Table():
    def __init__(self, deck, player):
        pass

deck = Deck()
deck.shuffle_deck()
player_hand = Hand()
print(deck)
