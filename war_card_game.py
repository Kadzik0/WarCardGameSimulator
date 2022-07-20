'''
WAR CARD GAME
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

game_cont=True
round_list=[]

class Card():

    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create tha card object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():

    def __init__(self, name='Unnamed'):
        self.name=name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type ([]):
            #List of multiple Card object
            self.all_cards.extend(new_cards)
        else:
            #For a single Card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return 'Player {} has {} cards'.format(self.name, len(self.all_cards))

def game():
    # GAME SETUP
    # define two players, deck and split the deck for them

    #define players
    player_1=Player(input('Sign in first player [name]: '))
    player_2=Player(input('Sign in second player [name]: '))

    #define deck
    deck_1=Deck()

    #shuffle defined deck
    deck_1.shuffle()

    #split the deck for players
    for index, value in enumerate(deck_1.all_cards):
        if index%2 == 0:
            player_1.all_cards.append(value)
        else:
            player_2.all_cards.append(value)

    # GAME ON
    # while game_on
    game_on = True
    game_round=1
    card_jackpot=[]

    while game_on:
        print(game_round)
        #check end/continue game condition
        if len(player_1.all_cards) == 0:
            game_on=False
            print('Player {} has won the game! Congratulations on your luck ;)! '. format(player_2.name))
            break
        elif len(player_2.all_cards) == 0:
            game_on=False
            print('Player {} has won the game! Congratulations on your luck ;)! '. format(player_1.name))
            break
        else:
            game_on=True

        #battle
        player_1_card=player_1.remove_one()
        player_2_card=player_2.remove_one()

        card_jackpot.append(player_1_card)
        card_jackpot.append(player_2_card)

        if player_1_card.value > player_2_card.value:
            player_1.add_cards(card_jackpot)
            card_jackpot=[]
        elif player_1_card.value < player_2_card.value:
            player_2.add_cards(card_jackpot)
            card_jackpot=[]
        elif player_1_card.value == player_2_card.value:
            if len(player_1.all_cards) == 0 or len(player_2.all_cards) == 0:
                pass
            else:
                card_jackpot.append(player_1.remove_one())
                card_jackpot.append(player_2.remove_one())               
        else:
            pass
        game_round+=1

        if game_round>=5000:
            print('remis')
            game_on=False
            print(player_1)
            print(player_2)
        else:
            pass  

    return(game_round)      


while game_cont:
    round_ctr=game()
    if round_ctr==5000:
        pass
    else:
        round_list.append(round_ctr)
        
    if (input('Do you want to play again? [Y/N] ')).upper()=='N':
        game_cont=False
    else:
        pass


print(round_list)
print('Avarage length of game was {}'.format(sum(round_list)/len(round_list)))




