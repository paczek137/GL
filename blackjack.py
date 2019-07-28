class Game:
    def __init__(self):
        print("Created Game")


class Blackjack(Game):
    def __init__(self):
        super().__init__()
        print("Created Blackjack")
        #self.cards = Cards()
        #print("as: " + str(self.cards.get_points("q")))
        #c = Card("leaves", "A")
        #c.print_card()
        player = Player()
        print("Points: " + str(player.get_points()))
        player.print_cards()
        #player.print_cards_vertical()


class Card:
    HEARTS = "hearts"
    BELLS = "bells"
    ACORNS = "acorns"
    LEAVES = "leaves"

    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

    DEFAULT_PATTERN = list("+-----+\n|     |\n|  ?  |\n|     |\n+-----+")

    def __init__(self, suit, value, hidden=False):
        self.points = None
        print("Created card")
        self.suit = suit
        self.value = value
        self.hidden = hidden
        self.pattern = self.DEFAULT_PATTERN.copy()
        self.init_points()
        if not self.hidden:
            self.init_card_pattern()

    def init_card_pattern(self):
        if self.suit == self.HEARTS:
            self.pattern[19] = "♥"
        elif self.suit == self.BELLS:
            self.pattern[19] = "♦"
        elif self.suit == self.ACORNS:
            self.pattern[19] = "♣"
        elif self.suit == self.LEAVES:
            self.pattern[19] = "♠"
        if self.value == self.TEN:
            self.pattern[10:12] = "10"
        else:
            self.pattern[11] = self.value

    def init_points(self):
        if self.value.isdigit():
            if int(self.value) in range(2, 11):
                self.points = int(self.value)
        elif self.value == self.JACK or self.value == self.QUEEN or self.value == self.KING:
            self.points = 10
        elif self.value == self.ACE:
            self.points = 11

    def print_card(self):
        print("".join(self.pattern))


class Player:
    def __init__(self):
        print("Created player")
        self.cards = []
        c1 = Card(Card.HEARTS, Card.FIVE)
        c2 = Card(Card.BELLS, Card.QUEEN)
        c3 = Card(Card.ACORNS, Card.TEN)
        c4 = Card(Card.LEAVES, Card.ACE)
        c5 = Card(Card.HEARTS, Card.THREE, True)
        self.add_new_card(c1)
        self.add_new_card(c2)
        self.add_new_card(c3)
        self.add_new_card(c4)
        self.add_new_card(c5)
        #self.cards.append(Card("hearts", "K"))

    def get_points(self):
        total_points = 0
        for c in self.cards:
            total_points = total_points + c.points
        return total_points

    def add_new_card(self, card):
        self.cards.append(card)

    def print_cards_vertical(self):
        for c in self.cards:
            c.print_card()

    def print_cards(self):
        cards_str = [""] * (5)
        for c in range(len(self.cards)):
            line_no = 0
            for line in "".join(self.cards[c].pattern).splitlines():
                cards_str[line_no] = cards_str[line_no] + line + "  "
                line_no = line_no + 1
            #print(cards_str)
            #"".join(c.pattern).splitlines()
            #cards_str = cards_str + "".join(c.pattern) + "\n"
        cards_presentation_str = ""
        for line in cards_str:
            cards_presentation_str = cards_presentation_str + line + "\n"
        print(cards_presentation_str)

# MAIN


bl = Blackjack()
