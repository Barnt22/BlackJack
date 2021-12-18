suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit
    def score(self):
        return values[self.rank]

class Deck:
    # upon calling for a deck, an array is created using two loops to create multiple cards
    # then shuffled
    # added a shuffle method
    def __init__(self):
        import random
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        random.shuffle(self.deck)
    
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
        rank = card.rank
        suit = card.suit
        return suit, rank

deck = Deck()
print(deck)
ace_of_hearts = Card(suits[0], ranks[-1])
print(ace_of_hearts.score)


# class Player:
#     pass

# class Dealer:
#     pass

# class Bots:
#     pass

# class Main:
#     pass