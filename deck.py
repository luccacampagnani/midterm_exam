import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♠️", "♥️", "♦️", "♣️"] # RANKS, SUITS are class attributes
    def __init__(self, suit, rank):
        """
        Initialising individual card & setting up  error detection
        :param suit: suit assigned from SUITS
        :param rank: rank assigned from RANKS
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._rank = rank
        self._suit = suit

    def __eq__(self, other):
        """
        'Equal to' dunder method to compare self (current instance of the card) with another card according to RANKS
        :param other: other card
        :return: boolean comparison
        """
        return self.rank == other.rank # .rank is a property defined below

    def __gt__(self, other):
        """
        Compares position of 'self' & 'other' in RANKS list to see which is greater
        :param other: other card
        :return: boolean comparison
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self): # str for when it will be put in a normal string
        """
        Sets how output will be displayed when shown as a string
        :return: string version displaying rank & suit of the card
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self): # use repr for when it will be put in a list
        """
        Sets the representation of self when printed
        :return: same as string output
        """
        return self.__str__()

    @property
    def suit(self):
        """
        Getter method to get value of suit attribute
        :return: value of self._suit that was initialised
        """
        return self._suit

    @property
    def rank(self):
        """
        Getter method to get value of rank attribute
        :return: value of self._rank that was initialised
        """
        return self._rank

class Deck:
    def __init__(self):
        """
        Deck is initialised; Cards appended to empty list using nested for loops
        """
        self._deck = []
        for suit in Card.SUITS: # first loop to assign suit
            for rank in Card.RANKS: # second loop to assign rank
                self._deck.append(Card(suit, rank)) # card created using Card class & appended to list

    def __str__(self):
        """
        Defines how string output of deck (for this given instance) will be displayed
        :return: string output
        """
        return str(self._deck)

    def shuffle(self):
        """
        Shuffles cards using .shuffle() from the random package; Changes order of the cards, as you would want in a real card game where chance is a factor
        :return: the original deck, but with the cards in a random order now
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        "Deals" a card by extracting the first card in the list; That card is now no longer in the list
        :return: only the first card in the deck
        """
        return self._deck.pop(0)

if __name__ == "__main__": # this section is only run when this is the main file
    deck = Deck() # deck created using Deck class; Uses functionalities from Card class within
    print(deck)
    deck.shuffle() # deck shuffled using .shuffle() method defined within the class Deck
    print(deck)
    print(deck.deal()) # first card in shuffled deck is dealt (done using .deal() method defined in class Deck)