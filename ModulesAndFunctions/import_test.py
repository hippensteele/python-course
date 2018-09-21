#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 14, 2018 7:14:06 AM$"

import blackjack2 as blackjack

print("__name__ from import_test.py: " + __name__)
#blackjack._deal_card(blackjack.dealer_card_frame) ## by convention, should never use methods prefixed with _ from imported modules
blackjack.play()
#print(blackjack.cards)