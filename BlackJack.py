suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
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

class Chips():
    def __init__(self, bank):
        self.total = bank
        self.bet = 0
    def __repr__(self):
        return str(self.total)
    def win_bet(self):
        self.chips += self.bet
    def lose_bet(self):
        self.chips -= self.bet
class Player():
    def __init__(self, chips, hand, name):
        self.chips = chips
        self.hand = hand
        self.name = name

    def __repr__(self):
        return """
        {name} has {chips} chips:
        {name}'s hand consists of:
        {hand}
        """.format(name = self.name, chips = str(self.chips), hand = str(self.hand))

def get_total_chip_ammount():
    while True:
        try:
            total = int(input("Enter how many chips you would like to start out with: "))
        except ValueError:
            print("ammount must be an integer!")
        else:
            break
    return total

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Enter a bet: "))
        except ValueError:
            print("Bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry your bet cannot exceed {}".format(chips.total))
            else:
                break

def hit_or_stand(Player):
    pass
def dealer_hit_or_stand(dealer_hand, deck):
    print("Dealer Score: \n{}".format(dealer_hand.score))
    if dealer_hand.score < 17:
        print("\nDealer Hits: ")
        new_card = deck.deal_card
        dealer_hand.add_card(new_card)
        print("\nDealer drew a {}:".format(new_card))
        print("\nDealer's score is now {}".format(dealer_hand.score))
    elif dealer_hand.score >= 17 and < 22:
        print("\nDealer cannot hit anymore: ")
        print("\nDealer score: {}".format(dealer_hand.score))
    else:
        print("Dealer ")
        



deck = Deck()
deck.shuffle_deck()
player_hand = Hand()
chip_ammount = get_total_chip_ammount()
chips = Chips(chip_ammount)
player = Player(chips, player_hand, "Player")
print(player)
print(deck)
