import collections
from random import choice

print(collections.__doc__)

Card = collections.namedtuple('Card', ['rank', 'suit'])

#print(Card)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        print(self.ranks)
        print(self.suits)
        return (self._cards)

'''The first thing to note is the use of collections.namedtuple to construct a simple class
    to represent individual cards.'''
beer_card = Card('7', 'diamonds')
print(beer_card)

'''like any standard Python collection, a deck responds to the len() function by
    returning the number of cards in it:'''
deck = FrenchDeck()
print(len(deck))

'''Reading specific cards from the deck—say, the first or the last—should be as easy as
   deck[0] or deck[-1], and this is what the __getitem__ method provides:'''
print(deck[0])
print(deck[-1])

'''Should we create a method to pick a random card? No need. Python already has a
    function to get a random item from a sequence: random.choice. We can just use it on
    a deck instance:'''
print(choice(deck))

'''Because our __getitem__ delegates to the [] operator of self._cards, our deck automatically
    supports slicing. Here’s how we look at the top three cards from a brand new
    deck, and then pick just the aces by starting on index 12 and skipping 13 cards at a time:'''
print(deck[:3])
print(deck[12::13])

'''Just by implementing the __getitem__ special method, our deck is also iterable:'''
#for card in deck:
#    print(card)

'''The deck can also be iterated in reverse:'''
for card in reversed(deck):
    print(card)

'''Iteration is often implicit. If a collection has no __contains__ method, the in operator
    does a sequential scan. Case in point: in works with our FrenchDeck class because it is
    iterable. Check it out:'''
print(Card('7', 'hearts') in deck)
print(Card('7', 'Furries') in deck)


'''How about sorting? A common system of ranking cards is by rank (with aces being
highest), then by suit in the order of spades (highest), then hearts, diamonds, and clubs
(lowest). Here is a function that ranks cards by that rule, returning 0 for the 2 of clubs
and 51 for the ace of spades:'''
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return  rank_value * len(suit_values) + suit_values[card.suit]

'''Given spades_high, we can now list our deck in order of increasing rank:'''
for card in sorted(deck, key=spades_high):
    print(card)




# print(deck.__repr__)