from deck import Deck, Card # Creating cards & deck is essential to starting the game - can import the classes we already set up in deck.py

class PokerHand:
    def __init__(self, deck):
        """
        Initialise deck with 5 cards for Poker
        :param deck: Deck that was created & shuffled using Deck class will be used to deal
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Getter method for cards list
        :return: list from self._cards
        """
        return self._cards

    def __str__(self):
        """
        Defining string display of cards list (with 5 cards)
        :return: string output
        """
        return str(self._cards)

# Checking for flush,
    @property # turns is_flush into a read-only property
    def is_flush(self):
        """
        Checking whether there is a flush in the 5 current five card hand
        :return: Boolean True or False
        """
        for card in self.cards[1:]: # loop from second card onwards
            if self.cards[0].suit != card.suit: # comparing 1st card suit to every other card suit
                return False
        return True

    @property
    def number_of_matches(self):
        """
        Counting number of matches in a hand based on how many cards have the same rank
        :return: number of matches
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)): # two loops mean each match is double counted (e.g. one pair is two matches, three of a kind is six matches & four of a kind is twelve matches)
                if i == j:
                    continue # skips comparing the card with itself
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1 # add 1 to match when two different cards in the hand have the same rank
        return matches

    @property
    def is_pair(self):
        """
        Checks whether there is one pair in the hand using number_of_matches property defined just before
        :return: Boolean True or False
        """
        if self.number_of_matches == 2: # one pair has two matches as per our number_of_matches property which uses double counting
            return True
        return False

    @property
    def is_two_pair(self):
        """
        Checks whether there are two separate pairs using number_of_matches
        :return: Boolean True or False
        """
        return self.number_of_matches == 4 # more complicated statement structure
# statement structure above is shorter than if, else; Returns True when conditional is satisfied & if not, automatically False

    @property
    def is_three_pair(self):
        """
        Checks whether there is a group of three identical rank cards using number_of_matches
        :return: Boolean True or False
        """
        return self.number_of_matches == 6

    @property
    def is_four_pair(self):
        """
        Checks whether there are four cards with an identical rank using number_of_matches
        :return: Boolean True or False
        """
        return self.number_of_matches == 12

# Full house = if is_three_pair & is_pair
    @property
    def is_full_house(self):
        """
        Checks for a full house --> when there is a three of a kind + a pair
        :return: True or False
        """
        return self.number_of_matches == 8 # 6 matches from three of a kind + 2 matches from a pair

    @property
    def is_straight(self):
        """
        Checks for a straight when five cards of any suit are in sequential order of rank
        :return:
        """
        self.cards.sort() # can sort by rank since __eq__ & __gt__ defined for Card class
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank) # if it is a 'straight' then when sorted the difference between the largest rank card and smallest rank card will be 4 (since there will only be five cards, all in order)
        return self.number_of_matches == 0 and distance == 4 # if 'straight', all cards will be different + (as explained above) difference between largest & smallest card rank in sorted hand will be 4

if __name__ == "__main__":
    count = 0 # number of times loop is run
    matches = 0 # number of times the characteristic we are seeking has occurred in these loops
    while matches < 1000: # keeps checking while total number of straights found is less than 1000
        deck = Deck()
        deck.shuffle()
        hand = PokerHand(deck)
        if hand.is_straight:
            matches += 1 # matches increased by one when hand is a straight
            print(hand)
        count += 1 # count increased by one regardless of whether it is a straight or not

    print(f"Probability of a straight flush is {100*matches/count}%")