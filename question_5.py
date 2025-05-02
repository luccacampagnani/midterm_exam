import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Card and Deck classes
class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♠️", "♥️", "♦️", "♣️"]

    def __init__(self, suit, rank):
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._rank = rank
        self._suit = suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__()

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

class Deck:
    def __init__(self):
        self._deck = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop(0)

# PokerHand with flush check
class PokerHand:
    def __init__(self, deck):
        self._cards = [deck.deal() for _ in range(5)]

    @property
    def cards(self):
        return self._cards

    @property
    def is_flush(self):
        suits = [card.suit for card in self.cards]
        return all(s == suits[0] for s in suits)

# Run simulation and plot
def run_simulation(num_iterations):
    flushes = 0
    x_vals = []
    y_vals = []

    for i in range(1, num_iterations + 1):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand(deck)
        if hand.is_flush:
            flushes += 1
        probability = (flushes / i) * 100
        x_vals.append(i)
        y_vals.append(probability)

    line.set_xdata(x_vals)
    line.set_ydata(y_vals)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

    print(f"Final Flush Probability: {round(probability, 4)}%")

# Set up initial plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = ax.plot([], [], label="Flush Probability (%)")
ax.set_xlabel("Number of Draws")
ax.set_ylabel("Probability (%)")
ax.set_title("Flush Probability Simulation")
ax.grid(True)
ax.legend()

# Slider setup
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, "Iterations", 1000, 50000, valinit=1000, valstep=100)

def update(val):
    run_simulation(int(slider.val))

slider.on_changed(update)

# Initial simulation
run_simulation(1000)
plt.show()
