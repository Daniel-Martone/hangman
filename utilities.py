def show_hangman(fails = 0):
    hangmans = [
'''|——————
|     |
|    
|
|
|_''',
'''|——————
|     |
|     O
|
|
|_''',
'''|——————
|     |
|     O  
|     |
|
|_''',
'''|——————
|     |
|     O  
|     |
|    /
|_''',
'''|——————
|     |
|     O  
|     |
|    / \ 
|_''',
'''|——————
|     |
|     O  
|     |\ 
|    / \ 
|_''',
'''|——————
|     |
|     X
|    /|\ 
|    / \ 
|_''']
    if fails > 6:
        fails = 6
    return f'{hangmans[fails]}            '

def gen_word():
    from random import choice
    words = ('homework', 'family', 'undestanding', 'event', 'friend', 'apple', 'magazine', 'fortune', 'opportunity', 'uncle', 'population', 'preference', 'diamond', 'sister', 'dirt', 'category', 'technology', 'piano')
    word = choice(words)
    return word

def show_word(word, letters):
    for c in word:
        if c in letters:
            print(c, end='')
        else:
            print('_', end='')
    print()
        
def read_letter(msg):
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    while True:
        letter = input(msg).lower().strip()
        if letter in letters:
            return letter
        print('ERROR')