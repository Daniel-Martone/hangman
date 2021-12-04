from utilities import *
errors = 0
right = 0
word = gen_word()
letters = set()
while True:
    print(show_hangman(errors), end='')
    show_word(word, letters)
    print(f'Letters used: ', end='')
    for c in letters:
        print(c.upper(), end=', ')
    print()
    letter = read_letter('Type a letter: ')
    if letter not in word and letter not in letters:
        errors += 1
    else:
        right += word.count(letter)
    letters.add(letter)
    letters = set(sorted(letters))
    if errors == 6:
        print(f'YOU LOST. The word was --> {word} <--')
        break
    if right == len(word):
        print(f'YOU WON! The word was --> {word} <--')
        break
    print('-=-'*10)