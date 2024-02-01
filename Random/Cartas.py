#!python3.6
# coding: utf8

import random

def Carta(valor, nipe):
    nipe = '♥♦♣♠'[nipe - 1]  # 1,2,3,4 = ♥♦♣♠
    print('┌───────┐')
    print(f'| {valor:<2}    |')
    print('|       |')
    print(f'|   {nipe}   |')
    print('|       |')
    print(f'|    {valor:>2} |')
    print('└───────┘')


while True:
    op = input("Enter para nova carta (x - terminar): ")
    if op == 'x':
        break
    Carta(random.choice(range(1, 12)), random.choice(range(1, 5)))

# class Card:
#     def __init__(self,value,suit):
#         self.value = value
#         self.suit = '♥♦♣♠'[suit-1] # 1,2,3,4 = ♥♦♣♠
#
#     def print(self):
#         print('┌───────┐')
#         print(f'| {self.value:<2}    |')
#         print('|       |')
#         print(f'|   {self.suit}   |')
#         print('|       |')
#         print(f'|    {self.value:>2} |')
#         print('└───────┘')
#
# x = Card('10',3)
# x.print()
