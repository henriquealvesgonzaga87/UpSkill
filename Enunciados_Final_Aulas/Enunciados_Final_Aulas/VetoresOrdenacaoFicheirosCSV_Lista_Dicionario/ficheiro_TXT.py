

# https://docs.python.org/pt-br/dev/library/fileinput.html
import fileinput
with fileinput.input(files=('names.csv', 'eggs.csv')) as f:
    for line in f:
        print(line)


# https://docs.python.org/pt-br/dev/library/persistence.html
