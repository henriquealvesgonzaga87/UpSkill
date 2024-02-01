import random

while True:
    op = input("Enter para lançar dado (x - terminar): ")
    if op == 'x':
        break
    n = random.randint(1, 6)
    print("Face:", n)

# v2
print("%c" % 0x1F3B2) # print('🎲')
while True:
    op = input("Enter para lançar dado (x - terminar): ")
    if op == 'x':
        break
    n = random.choice(range(0x2680, 0x2685+1))
    print("Face: %c" % n)

# Using Unicode characters, the faces can be shown in text using the range U+2680 to U+2685
# ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ 🎲

# Enter para lançar dado (x - terminar):
# Face: 6
# Enter para lançar dado (x - terminar):
# Face: 1
# Enter para lançar dado (x - terminar):
# Face: 4
# Enter para lançar dado (x - terminar):
# Face: 5
# Enter para lançar dado (x - terminar):
# Face: 5
# Enter para lançar dado (x - terminar):
# Face: 2
# Enter para lançar dado (x - terminar):

