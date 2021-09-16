class Card:
    def __init__(self, name, value, suit, color) -> None:
        self.name = name
        self.value = value
        self.suit = suit
        self.color = color
    
    def __str__(self):
        return f'{self.name} of {self.suit}'


two_of_hearts = Card('two', 2, 'hearts', 'red')
two_of_diamonds = Card('two', 2, 'diamonds', 'red')
two_of_spades = Card('two', 2, 'spades', 'black')
two_of_clubs = Card('two', 2, 'clubs', 'black')

three_of_hearts = Card('three', 3, 'hearts', 'red')
three_of_diamonds = Card('three', 3, 'diamonds', 'red')
three_of_spades = Card('three', 3, 'spades', 'black')
three_of_clubs = Card('three', 3, 'clubs', 'black')

four_of_hearts = Card('four', 4, 'hearts', 'red')
four_of_diamonds = Card('four', 4, 'diamonds', 'red')
four_of_spades = Card('four', 4, 'spades', 'black')
four_of_clubs = Card('four', 4, 'clubs', 'black')

five_of_hearts = Card('five', 5, 'hearts', 'red')
five_of_diamonds = Card('five', 5, 'diamonds', 'red')
five_of_spades = Card('five', 5, 'spades', 'black')
five_of_clubs = Card('five', 5, 'clubs', 'black')

six_of_hearts = Card('six', 6, 'hearts', 'red')
six_of_diamonds = Card('six', 6, 'diamonds', 'red')
six_of_spades = Card('six', 6, 'spades', 'black')
six_of_clubs = Card('six', 6, 'clubs', 'black')

seven_of_hearts = Card('seven', 7, 'hearts', 'red')
seven_of_diamonds = Card('seven', 7, 'diamonds', 'red')
seven_of_spades = Card('seven', 7, 'spades', 'black')
seven_of_clubs = Card('seven', 7, 'clubs', 'black')

eight_of_hearts = Card('eight', 8, 'hearts', 'red')
eight_of_diamonds = Card('eight', 8, 'diamonds', 'red')
eight_of_spades = Card('eight', 8, 'spades', 'black')
eight_of_clubs = Card('eight', 8, 'clubs', 'black')

nine_of_hearts = Card('nine', 9, 'hearts', 'red')
nine_of_diamonds = Card('nine', 9, 'diamonds', 'red')
nine_of_spades = Card('nine', 9, 'spades', 'black')
nine_of_clubs = Card('nine', 9, 'clubs', 'black')

ten_of_hearts = Card('ten', 10, 'hearts', 'red')
ten_of_diamonds = Card('ten', 10, 'diamonds', 'red')
ten_of_spades = Card('ten', 10, 'spades', 'black')
ten_of_clubs = Card('ten', 10, 'clubs', 'black')

jack_of_hearts = Card('jack', 10, 'hearts', 'red')
jack_of_diamonds = Card('jack', 10, 'diamonds', 'red')
jack_of_spades = Card('jack', 10, 'spades', 'black')
jack_of_clubs = Card('jack', 10, 'clubs', 'black')

queen_of_hearts = Card('queen', 10, 'hearts', 'red')
queen_of_diamonds = Card('queen', 10, 'diamonds', 'red')
queen_of_spades = Card('queen', 10, 'spades', 'black')
queen_of_clubs = Card('queen', 10, 'clubs', 'black')

king_of_hearts = Card('king', 10, 'hearts', 'red')
king_of_diamonds = Card('king', 10, 'diamonds', 'red')
king_of_spades = Card('king', 10, 'spades', 'black')
king_of_clubs = Card('king', 10, 'clubs', 'black')

ace_of_hearts = Card('ace', 11, 'hearts', 'red')
ace_of_diamonds = Card('ace', 11, 'diamonds', 'red')
ace_of_spades = Card('ace', 11, 'spades', 'black')
ace_of_clubs = Card('ace', 11, 'clubs', 'black')


deck_of_cards = [
two_of_hearts, two_of_diamonds, two_of_clubs, two_of_spades, 
three_of_hearts, three_of_diamonds, three_of_clubs, three_of_spades,
four_of_hearts, four_of_diamonds, four_of_clubs, four_of_spades,
five_of_hearts, five_of_diamonds, five_of_clubs, five_of_spades,
six_of_hearts, six_of_diamonds, six_of_clubs, six_of_spades,
seven_of_hearts, seven_of_diamonds, seven_of_clubs, seven_of_spades,
eight_of_hearts, eight_of_diamonds, eight_of_clubs, eight_of_spades,
nine_of_hearts, nine_of_diamonds, nine_of_clubs, nine_of_spades,
ten_of_hearts, ten_of_diamonds, ten_of_clubs, ten_of_spades,
jack_of_hearts, jack_of_diamonds, jack_of_clubs, jack_of_spades,
queen_of_hearts, queen_of_diamonds, queen_of_clubs, queen_of_spades,
king_of_hearts, king_of_diamonds, king_of_clubs, king_of_spades,
ace_of_hearts, ace_of_diamonds, ace_of_clubs, ace_of_spades
]



if __name__ == 'main': 

    print(deck_of_cards[0])
    print(deck_of_cards[1])
    print(deck_of_cards[2])
    print(deck_of_cards[3])
    deck_of_cards.append(deck_of_cards[0])
    deck_of_cards.append(deck_of_cards[1])
    deck_of_cards.append(deck_of_cards[2])
    deck_of_cards.append(deck_of_cards[3])
    deck_of_cards.pop(0)
    deck_of_cards.pop(0)
    deck_of_cards.pop(0)
    deck_of_cards.pop(0)
    print(deck_of_cards[0])
    print(deck_of_cards[1])
    print(deck_of_cards[2])
    print(deck_of_cards[3])
    print(deck_of_cards[-1])
    print(deck_of_cards[-2])
    print(deck_of_cards[-3])
    print(deck_of_cards[-4])