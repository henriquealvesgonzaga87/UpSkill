# https://python-course.eu/python-tutorial/errors-and-exception-handling.php

#n = int(input("Please enter a number: "))
#With the aid of exception handling, we can write robust code for reading an integer from input:



def int_input(prompt):
    while True:
        try:
            age = int(input(prompt))
            return age
        except ValueError as e:
            print("Not a proper integer! Try it again")

idade = int_input('Idade?')



while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError as e:
        print("No valid integer! Please try again ...")
        print("Informação do erro:", e)

print("Great, you successfully entered an integer!")

