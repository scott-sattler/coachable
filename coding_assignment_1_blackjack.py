# !!    python: List -> list | in "def _get_score(self, hand: List[Card]) -> int:"
# !!    typo: randomzing -> randomizing | in "Shuffles the deck of cards. This means randomizing the order of..."

# !!    design: swap suit: str <-> value: str | in Card __init__ params in def __init__(self, value: str, suit: str):
# !!    design: swap Card.value <-> Card.suit | in Card methods

# !!    typo: it's -> its | in Deck class "# Resets the deck to it's original state with all 52 cards."

# !?    design: shouldn't SUITS and VALUES be immutable/tuples?
# !?    design: SUITS and VALUES should be class variables?

# Question: boundary condition: > boundary or == boundary preferable?

import random
from random import randint


class Card:

    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, value: str, suit: str):
        # motivation, order: "Ace of Spades"
        self.card = (value, suit)

    # Returns the value of the card.
    def value(self) -> str:
        return self.card[0]

    # Returns the suit of the card.
    def suit(self) -> str:
        return self.card[1]

    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self) -> str:
        return f"{self.card[0]} of {self.card[1]}"


class Deck:
    # class variables
    SUITS = ("Diamonds", "Spades", "Hearts", "Clubs")
    VALUES = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
              "King")

    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    def __init__(self):
        self.deck = None
        self.reset()

    # Returns the number of Cards in the Deck
    def size(self) -> int:
        return len(self.deck)

    # Shuffles the deck of cards. This means randomizing the order of the cards in the Deck.
    def shuffle(self) -> None:
        random.shuffle(self.deck)

    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self) -> Card:
        return self.deck[-1]

    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self) -> Card:
        return self.deck.pop()

    # Adds the input card to the deck.
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card: Card) -> None:
        if len(self.deck) > 51:
            raise Exception
        else:
            self.deck.append(card)

    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self) -> None:
        for each_card in self.deck:
            print(each_card.__str__())

    # Resets the deck to its original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self) -> None:
        self.deck = [Card(value, suit) for value in self.VALUES for suit in self.SUITS]
        self.shuffle()


class Blackjack:
    # Creates a Blackjack game with a new Deck.
    def __init__(self):
        self.game_deck = Deck().deck
        self.current_hand = []
        self.discard_pile = []

    # Computes the score of a hand.
    # For examples of hands and scores as a number.
    # 2,5 -> 7
    # 3, 10 -> 13
    # 5, King -> 15
    # 10, Ace -> 21
    # 10, 8, 4 -> Bust so return -1
    # 9, Jack, Ace -> 20
    # If the Hand is a bust return -1 (because it always loses)
    def _get_score(self, hand: list[Card]) -> int:
        # todo move
        card_value = {k: v if v < 11 else 10 for v, k in enumerate(Deck.VALUES, start=1)}
        card_value["Ace"] = (card_value["Ace"], 11)

        score = 0
        has_ace = False
        for each_card in self.current_hand:
            card_string = each_card.__str__().split()[0]  # get first word (value)
            if "Ace" in card_string:
                has_ace = True
                score += 1
            else:
                score += card_value[card_string]
        if has_ace and score + 10 < 22:
            score += 10

        if score > 21:
            score = -1

        return score

    # Prints the current hand and score.
    # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
    # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
    def _print_current_hand(self) -> None:
        for each_card in self.current_hand:
            print(each_card.__str__(), end=", ")
        print(self._get_score(self.current_hand))

    # The previous hand is discarded and shuffled back into the deck.
    # Should remove the top 2 cards from the current deck and
    # Set those 2 cards as the "current hand".
    # It should also print the current hand and score of that hand.
    # If less than 2 cards are in the deck,
    # then print an error instructing the client to shuffle the deck.
    def deal_new_hand(self) -> None:
        if len(self.game_deck) < 2:
            print("Game Error: Only 1 card remaining. Reshuffle to continue playing.")
        self.current_hand.append(self.game_deck.pop())
        self.current_hand.append(self.game_deck.pop())
        self._print_current_hand()

    # Deals one more card to the current hand and prints the hand and score.
    # If no cards remain in the deck, print an error.
    def hit(self) -> None:
        if len(self.game_deck) == 0:
            print("Game Error: No cards remaining. Reshuffle to continue.")
        else:
            self.current_hand.append(self.game_deck.pop())
        self._print_current_hand()

    # Reshuffles all cards in the "current hand" and "discard pile"
    # and shuffles everything back into the Deck.
    def reshuffle(self) -> None:
        self.game_deck = self.game_deck + self.discard_pile
        random.shuffle(self.game_deck)


if __name__ == "__main__":
    playing = False
    blackjack = Blackjack()
    while playing:
        user_input = input("Enter Command: ")

        match user_input.lower():
            case "new":
                blackjack = Blackjack()
                print("New game.")
            case "deal":
                blackjack.deal_new_hand()
            case "hit":
                blackjack.hit()
            case "shuffle":
                blackjack.reshuffle()
            case "exit":
                playing = False


    def score_test() -> None:
        raise NotImplementedError

    score_test()





        # string_out = ""
        # for i, each_card in enumerate(self.deck):
        #     card = each_card.__str__()
        #     if i > 1 and i % 4 == 3:
        #         string_out += (card + '\n')
        #     else:
        #         string_out += (card + " " * (30 - len(card)))
        # print(string_out)

        # two list Fisher-Yates shuffle
        # shuffled_deck = []
        # while len(self.deck) > 0:
        #     if len(self.deck) > 1:
        #         index = randint(0, len(self.deck) - 1)
        #         self.deck[index], self.deck[-1] = self.deck[-1], self.deck[index]
        #     shuffled_deck.append(self.deck.pop())
        # self.deck = shuffled_deck