import random


# https://pynative.com/python-random-choice/
# random.choice(list)	Choose a random item from a sequence. Here seq can be a list, tuple, string, or any iterable like range.
# random.choices(list, k=3)	Choose multiple random items from a list, set, or any data structure.

r = random.choice(range(1,7))
print(r)
r = random.choices(range(1,10), k=7)  # pode repetir números
print(r)


# Creating function to roll the dices
def roll_dices():
     # These values indicate dots on the dices.
     # For eg: \u2680 corresponds to 1 dot,
     # \u2681 corresponds to 2 dots etc.
    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    # Generating random dots on the dices
    return random.choice(dice_dots)

while True:
    op = input("Enter para lançar dado (x - terminar): ")
    if op == 'x':
        break
    print(roll_dices())
