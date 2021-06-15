# INTERACTIONS BETWEEN PYTHON FUNCTIONS
my_list = ['', 'o', '']


def shuffle_list(my_list):
    shuffle(my_list)

    return my_list


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = (input("please choose a number: 0,1 or 2"))
    return int(guess)


def check_guess(my_list, guess):
    if my_list[guess] == 'o':
        print('correct guess!')
    else:
        print('wrong! better luck next time')
        print(my_list)


my_list = ['', 'o', '']
mixedup_list = shuffle_list(my_list)
guess = player_guess()
print(check_guess(mixedup_list, guess))
 