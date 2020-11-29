"""
A game where the player can choose to either guess a number or a word.
"""


import random


def main():
    name = input('What is your name? ')
    category = input(f'Would you like to guess a number or a word {name}?\nNumber or Word: ')
    if category == 'Number':
        number_guess()
    elif category == 'Word':
        word_guess()
    else:
        print(f'{category} is not a valid option.\nTry again.')
        main()


def word_guess():
    word_choices = ['monkey', 'potato', 'water', 'hentai', 'crypt']
    player_guess_word = ''
    secret_word = random.choice(word_choices)
    tries = 8

    while player_guess_word != secret_word:
        tries -= 1
        print(f'The word has {len(secret_word)} letters.')
        player_guess_word = input(f'You have {tries} tries.\nIf you need help, type "hint"\nGuess a word: ')
        if player_guess_word == 'hint':
            if secret_word == 'monkey':
                hints_monkey = ["It's an animal.", "It's part of the Chinese zodiac", 'It is said we evolved from them.']
                print(random.choice(hints_monkey))
            elif secret_word == 'potato':
                hints_potato = ['Ireland is famous for them.', 'Idaho is famous for them.',
                                'They are mashed and eaten at Thanksgiving.']
                print(random.choice(hints_potato))
            elif secret_word == 'water':
                hints_water = ['You need to drink this everyday.', 'The world is 70% of this stuff.',
                               'Your body is  60% of this stuff.']
                print(random.choice(hints_water))
            elif secret_word == 'hentai':
                hints_hentai = ["It's a kind of porn", 'Japanese', 'Thighs.']
                print(random.choice(hints_hentai))
            elif secret_word == 'crypt':
                hints_crypt = ['Another word for tomb and vault', 'A stone chamber', 'Egyptian burial chamber.']
                print(random.choice(hints_crypt))
    print(f'The word was {secret_word}. You win.')


def number_guess():
    secret_number = random.randint(0, 100)
    player_guess_number = " "
    tries = 0

    while player_guess_number != secret_number:
        tries += 1
        player_guess_number = int(input('Guess a number 0 - 100: '))
        if player_guess_number > secret_number:
            print(f'{player_guess_number} is too high.\nGuess lower.\n')
        else:
            print(f'{player_guess_number} is too low.\nGuess higher.\n')
    print(f'{player_guess_number} is correct.\nIt took {tries} tries.')


main()
