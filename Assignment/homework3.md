'''python
"""
Name: Zhiqi Mao
Email: zhiqimao@qq.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 17 Feb @ 5:00 p.m.
"""


# -*- coding: utf-8 -*-
import os
import sys
import time
import random

#Source: http://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards

CARD = """\
┌───────┐
│{}           │
│              │
│      {}     │
│              │
│           {}│
└───────┘
""".format('{trank:^2}', '{suit: <2}', '{brank:^2}')

TEN = """\
┌───────┐
│{}           │
│              │
│       {}     │
│              │
│           {}│
└───────┘
""".format('{trank:^3}', '{suit: <2}', '{brank:^3}')

FACECARD = """\
┌───────┐
│{}      │
│              │
│      {}     │
│              │
│      {}│
└───────┘
""".format('{trank:<7}', '{suit: <2}', '{brank:>7}')

HIDDEN_CARD = """\
┌───────┐
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
└───────┘
"""

class Card(object):

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """

        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]



        self.card_values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10,
            'Ace': 11,  # value of the ace is high until it needs to be low
        }

        self.str_values = {
            '2': CARD,
            '3': CARD,
            '4': CARD,
            '5': CARD,
            '6': CARD,
            '7': CARD,
            '8': CARD,
            '9': CARD,
            '10': TEN,
            'Jack': FACECARD,
            'Queen': FACECARD,
            'King': FACECARD,
            'Ace': FACECARD,  # value of the ace is high until it needs to be low
        }

        self.suits = ['Spades','Hearts','Diamonds','Clubs']

        self.symbols = {
            'Spades':   '♠',
            'Diamonds': '♦',
            'Hearts':   '♥',
            'Clubs':    '♣',
        }


        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit.capitalize()
        self.rank = str(rank)
        self.symbol = self.symbols[self.suit]
        self.points = self.card_values[str(rank)]
        self.ascii = self.__str__()


    def __str__(self):
        symbol = self.symbols[self.suit]
        trank = self.rank+symbol
        brank = symbol+self.rank
        return self.str_values[self.rank].format(trank=trank, suit=symbol,brank=brank)

    def __cmp__(self,other):

        return self.ranks.index(self.rank) < self.ranks.index(other.rank)

    # Python3 wasn't liking the __cmp__ to sort the cards, so
    # documentation told me to use the __lt__ (less than)
    # method.
    def __lt__(self,other):
        return self.__cmp__(other)

"""
@Class Deck
@Description:
    This class represents a deck of cards.
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""
class Deck(object):
    def __init__(self):
        #assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]:
                self.cards.append(Card(suit,rank))

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "".join(res)

    def pop_card(self):
        return self.cards.pop(0)

    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards = sorted(self.cards)

class Hand(list):
    def __init__(self, cards=None):
        """Initialize the class"""
        super().__init__()
        if (cards is not None):
            self._list = list(cards)
        else:
            self._list = []

    def __str__(self):
        return self.join_lines()

    def join_lines(self):
        """
        Stack strings horizontally.
        This doesn't keep lines aligned unless the preceding lines have the same length.
        :param strings: Strings to stack
        :return: String consisting of the horizontally stacked input
        """
        liness = [card.ascii.splitlines() for card in self._list]
        return '\n'.join(''.join(lines) for lines in zip(*liness))

    def add(self,card):
        self._list.append(card)

    def sort(self):
        self._list = sorted(self._list)

    def __getitem__(self,key):
        return self._list[key]



class Player(list):
    def deal(self):
        #Start the game with 26 cards in player's hand and 26 cards in computer's hand
        global H, C
        D=Deck()
        H=Hand()
        C=Hand()
        D.shuffle()
        for i in range(26):
            H.add(D.pop_card())
            C.add(D.pop_card())


    def war(self):
        round=0
        hcount=26
        ccount=26
        while H and C:
            player1=H._list.pop(0)
            player2=C._list.pop(0)
            print('Player 1 Card: \n', player1)
            print('Computer Card: \n', player2)
            if player1 > player2:
                print('Player 1 Won')
                H.add(player1)
                H.add(player2)
                ccount = ccount-1
                hcount = hcount+1
                round+=1
            elif player1 < player2:
                print('Computer Won')
                C.add(player1)
                C.add(player2)
                ccount = ccount+1
                hcount = hcount-1
                round+=1
            else:
                draw=Hand()
                while player1 == player2:
                    print('Tie, draw one card, and flip the next card')
                    time.sleep(3)
                    print(HIDDEN_CARD,HIDDEN_CARD)
                    draw.add(player1)
                    draw.add(player2)
                    draw.add(H._list.pop(0))
                    draw.add(H._list.pop(0))
                    player1=H._list.pop(0)
                    player2=H._list.pop(0)
                    print('Player 1 Card: \n', player1)
                    print('Computer Card: \n', player2)

                if player1>player2:
                    print('Player 1 Won')
                    add1=1
                else:
                    print('Computer Won')
                    add1=0

                if add1:
                    while draw:
                        H.add(draw._list.pop(0))
                        ccount = ccount-1
                        hcount = hcount+1
                else:
                    while draw:
                        C.add(draw._list.pop(0))
                        ccount = ccount+1
                        hcount = hcount-1
            print('This is round ', round)
            print('Player 1 has ',hcount,'card(s)')
            print('Computer has ',ccount,'card(s)')
            time.sleep(3)

            if hcount == 0:
                print('Congratulations for winning the game')
                os.system("pause")
                sys.exit(0)
            elif ccount ==0:
                print('Sorry, you lose the game')
                os.system("pause")
                sys.exit(0)

class Game(list):
    def deal(self):
        #Start the game with 26 cards in player1's hand and 26 cards in player2's hand
        global H, C
        D=Deck()
        H=Hand()
        C=Hand()
        D.shuffle()
        for i in range(26):
            H.add(D.pop_card())
            C.add(D.pop_card())


    def war(self):
        round=0
        hcount=26
        ccount=26
        while H and C:
            player1=H._list.pop(0)
            player2=C._list.pop(0)
            print('Player 1 Card: \n', player1)
            print('Player 2 Card: \n', player2)
            if player1 > player2:
                print('Player 1 Won')
                H.add(player1)
                H.add(player2)
                ccount = ccount-1
                hcount = hcount+1
                round+=1
            elif player1 < player2:
                print('Player 2 Won')
                C.add(player1)
                C.add(player2)
                ccount = ccount+1
                hcount = hcount-1
                round+=1
            else:
                draw=Hand()
                while player1 == player2:
                    print('Tie, draw one card, and flip the next card')
                    print(HIDDEN_CARD,HIDDEN_CARD)
                    draw.add(player1)
                    draw.add(player2)
                    draw.add(H._list.pop(0))
                    draw.add(H._list.pop(0))
                    player1=H._list.pop(0)
                    player2=H._list.pop(0)
                    print('Player 1 Card: \n', player1)
                    print('Player 2 Card: \n', player2)

                if player1>player2:
                    print('Player 1 Won')
                    add1=1
                else:
                    print('Player 2 Won')
                    add1=0

                if add1:
                    while draw:
                        H.add(draw._list.pop(0))
                        ccount = ccount-1
                        hcount = hcount+1
                else:
                    while draw:
                        C.add(draw._list.pop(0))
                        ccount = ccount+1
                        hcount = hcount-1
                        print('This is round ', round)
                print('Player 1 has ',hcount,'card(s)')
                print('Player 2 has ',ccount,'card(s)')
                time.sleep(3)

            if hcount == 0:
                print('Congratulations for Player 2 won the game')
                os.system("pause")
                sys.exit(0)
            elif ccount ==0:
                print('Congratulations for Player 1 won the game')
                os.system("pause")
                sys.exit(0)

choose = 0
while choose == 0:
    print('Please select game type by typing the number in front: \n 1. Single Player \n 2. Double Player')
    choose = input('Enter your choice: ')
    if choose == 1:
        print('Entering single player mode, please wait while game is loading...')
        time.sleep(5)
    elif choose ==2:
        print('Entering double player mode, please wait while game is loading...')
        time.sleep(5)
    else:
        choose = 0
        print('Choice was invalid, please input 1 or 2')
        print('Please select game type: \n 1. Single Player \n 2. Double Player')
        choose = input('Enter your choice: ')

if choose == 1:
    Player.deal(Deck())
    Player.war(Deck())
else:
    Game.deal(Deck())
    Game.war(Deck())
'''
