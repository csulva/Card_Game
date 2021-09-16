# Imports
from hashlib import new
import cards as c
import random
import time

# War Card Game

# Randomize Deck
random.shuffle(c.deck_of_cards)

# Logic of values of cards
for x in c.deck_of_cards:
    if x.name == 'jack':
        x.value = 10.1
    if x.name == 'queen':
        x.value = 10.2
    if x.name == 'king':
        x.value = 10.3


# Split by 2-4 players
players = input('How many players would like to play? Select between 2 and 4: ')
if players == '2':
    player_one_cards = list(c.deck_of_cards[0::2])
    player_two_cards = list(c.deck_of_cards[1::2])
# if players == '3':
#     player_one_cards = list(c.deck_of_cards[0::3])
#     player_two_cards = list(c.deck_of_cards[1::3])
#     player_three_cards = list(c.deck_of_cards[2::3])
# if players == '4':
#     player_one_cards = list(c.deck_of_cards[0::4])
#     player_two_cards = list(c.deck_of_cards[1::4])
#     player_three_cards = list(c.deck_of_cards[2::4])
#     player_four_cards = list(c.deck_of_cards[3::4])

player_one = input('What is player one\'s name? ')
player_two = input('What is player two\'s name? ')
print(f'Welcome {player_one} and {player_two}.')

# Define gameplay
def play():
    play_game = input('Press enter to play the hand: ')
    # Display each person's top card
    print(f'{player_one} plays the <{player_one_cards[0]}> and {player_two} plays the <{player_two_cards[0]}>')
    if player_one_cards[0].value > player_two_cards[0].value:
        player_one_cards.append(player_two_cards[0])
        time.sleep(2)
        print(f'{player_one} wins the {player_two_cards[0]}!')
        player_one_cards.append(player_one_cards[0])
        player_one_cards.pop(0)
        player_two_cards.pop(0)
        print(f'{player_one}\'s cards: {len(player_one_cards)}')
        print(f'{player_two}\'s cards: {len(player_two_cards)}')
    elif player_one_cards[0].value < player_two_cards[0].value:
        player_two_cards.append(player_one_cards[0])
        time.sleep(2)
        print(f'{player_two} wins the {player_one_cards[0]}!')
        player_two_cards.append(player_two_cards[0])
        player_two_cards.pop(0)
        player_one_cards.pop(0)
        print(f'{player_one}\'s cards: {len(player_one_cards)}')
        print(f'{player_two}\'s cards: {len(player_two_cards)}')
    elif player_one_cards[0].value == player_two_cards[0].value:
        draw()
    # What happens when you lose
    if len(player_one_cards) == 0:
        print(f'{player_two} has won!!')
        quit
    elif len(player_two_cards) == 0:
        print(f'{player_one} has won!!')
        quit

# What happens if there is a tie
def draw():
    draw = (f'It\'s a tie! We must draw your next three cards to see who wins... ')
    time.sleep(2)
    print(f'{player_one} throws the <{player_one_cards[1]}>, the <{player_one_cards[2]}> and plays the <{player_one_cards[3]}>!')
    time.sleep(2)
    print(f'{player_two} throws the <{player_two_cards[1]}>, the <{player_two_cards[2]}> and plays the <{player_two_cards[3]}>!')
    if player_one_cards[3].value > player_two_cards[3].value:
        player_one_cards.append(player_two_cards[0])
        player_one_cards.append(player_two_cards[1])
        player_one_cards.append(player_two_cards[2])
        player_one_cards.append(player_two_cards[3])
        print(f'{player_one} wins the <{player_two_cards[0]}>, the <{player_two_cards[1]}>, the <{player_two_cards[2]}>, AND the <{player_two_cards[3]}>')
        player_two_cards.pop(0)
        player_two_cards.pop(1)
        player_two_cards.pop(2)
        player_two_cards.pop(3)
        player_one_cards.append(player_one_cards[0])
        player_one_cards.append(player_one_cards[1])
        player_one_cards.append(player_one_cards[2])
        player_one_cards.append(player_one_cards[3])
        player_one_cards.pop(0)
        player_one_cards.pop(1)
        player_one_cards.pop(2)
        player_one_cards.pop(3)
        print(f'{player_one} cards: {len(player_one_cards)}')
        print(f'{player_two} cards: {len(player_two_cards)}')
    elif player_one_cards[3].value < player_two_cards[3].value:
        player_two_cards.append(player_one_cards[0])
        player_two_cards.append(player_one_cards[1])
        player_two_cards.append(player_one_cards[2])
        player_two_cards.append(player_one_cards[3])
        print(f'{player_two} wins the <{player_one_cards[0]}>, the <{player_one_cards[1]}>, the <{player_one_cards[2]}>, AND the <{player_one_cards[3]}>')
        player_one_cards.pop(0)
        player_one_cards.pop(1)
        player_one_cards.pop(2)
        player_one_cards.pop(3)
        player_two_cards.append(player_two_cards[0])
        player_two_cards.append(player_two_cards[1])
        player_two_cards.append(player_two_cards[2])
        player_two_cards.append(player_two_cards[3])
        player_two_cards.pop(0)
        player_two_cards.pop(1)
        player_two_cards.pop(2)
        player_two_cards.pop(3)
        print(f'{player_one} cards: {len(player_one_cards)}')
        print(f'{player_two} cards: {len(player_two_cards)}')
    elif player_one_cards[3] == player_two_cards[3]:
        draw_two = (f'It\'s ANOTHER tie! We must draw your next card to see who wins... ')
        time.sleep(2)
        print(f'{player_one} throws a <{player_one_cards[4]}>!')
        time.sleep(2)
        print(f'{player_two} throws a <{player_two_cards[1]}>!')
        if player_one_cards[4].value > player_two_cards[4].value:
            player_one_cards.append(player_two_cards[0])
            player_one_cards.append(player_two_cards[1])
            player_one_cards.append(player_two_cards[2])
            player_one_cards.append(player_two_cards[3])
            player_one_cards.append(player_two_cards[4])
            print(f'{player_one} wins the <{player_two_cards[0]}>, the <{player_two_cards[1]}>, the <{player_two_cards[2]}>, the <{player_two_cards[3]}>, AND the <{player_two_cards[4]}!')
            player_two_cards.pop(0)
            player_two_cards.pop(1)
            player_two_cards.pop(2)
            player_two_cards.pop(3)
            player_two_cards.pop(4)
            player_one_cards.append(player_one_cards[0])
            player_one_cards.append(player_one_cards[1])
            player_one_cards.append(player_one_cards[2])
            player_one_cards.append(player_one_cards[3])
            player_one_cards.append(player_one_cards[4])
            player_one_cards.pop(0)
            player_one_cards.pop(1)
            player_one_cards.pop(2)
            player_one_cards.pop(3)
            player_one_cards.pop(4)
            print(f'{player_one} cards: {len(player_one_cards)}')
            print(f'{player_two} cards: {len(player_two_cards)}')
        elif player_one_cards[4].value < player_two_cards[4].value:
            player_two_cards.append(player_one_cards[0])
            player_two_cards.append(player_one_cards[1])
            player_two_cards.append(player_one_cards[2])
            player_two_cards.append(player_one_cards[3])
            player_two_cards.append(player_one_cards[4])
            print(f'{player_two} wins the <{player_one_cards[0]}>, the <{player_one_cards[1]}>, the <{player_one_cards[2]}>, the <{player_one_cards[3]}>, AND the {player_one_cards[4]}!')
            player_one_cards.pop(0)
            player_one_cards.pop(1)
            player_one_cards.pop(2)
            player_one_cards.pop(3)
            player_one_cards.pop(4)
            player_two_cards.append(player_two_cards[0])
            player_two_cards.append(player_two_cards[1])
            player_two_cards.append(player_two_cards[2])
            player_two_cards.append(player_two_cards[3])
            player_two_cards.append(player_two_cards[4])
            player_two_cards.pop(0)
            player_two_cards.pop(1)
            player_two_cards.pop(2)
            player_two_cards.pop(3)
            player_two_cards.pop(4)
            print(f'{player_one} cards: {len(player_one_cards)}')
            print(f'{player_two} cards: {len(player_two_cards)}')


# Play the game
while len(player_one_cards):
    play()
