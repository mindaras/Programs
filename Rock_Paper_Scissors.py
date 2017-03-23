from random import randint

values = ['rock', 'paper', 'scissors']
indexes = []
win = '\nYou won \n'
lose = '\nYou lost \n'
tie = '\nIt\'s a tie \n'
user_score = 0
computer_score = 0

for i, items in enumerate(values):
    print (i, items)
    indexes.append(i)
print ()

a = 0
r = 'y'
while r == 'y':
    while a < 3:
        try:
            a += 1
            users_value = input('\nWhat\'s your choice: ')
            users_value = int(users_value)
            computers_value = randint(0, 2)
    
            print ('You chose ' + values[users_value])
            print ('Computer chose ' + values[computers_value])
            if users_value == 0 and computers_value ==  2 or users_value == 1 and \
                computers_value == 0 or users_value == 2 and computers_value == 1:
                print(win)
                user_score += 1
            elif users_value == computers_value:
                print(tie)
            else:
                print(lose)
                computer_score += 1
        except(IndexError, ValueError):
            print('Invalid value.')
            a -= 1

    print('Your score: %s Computer\'s score: %s' % (user_score, computer_score))

    d = {
        'y' : 'y',
        'n' : 'n'
        }
    
    if user_score > computer_score:
        print('Congratulations! You have won!')
        r = input('\nWant to try again? y/n: ')
        while r not in d:
            r = input('\nInvalid value.\nWant to try again? y/n: ')
        else:
            a = 0
            user_score = 0
            computer_score = 0
    elif user_score == computer_score:
        print('I\'s a tie!')
        r = input('\nWant to try again? y/n: ')
        while r not in d:
            r = input('\nInvalid value.\nWant to try again? y/n: ')
        else:
            a = 0
            user_score = 0
            computer_score = 0
    else:
        print('Sorry, You have lost!')
        r = input('\nWant to try again? y/n: ')
        while r not in d:
            r = input('\nInvalid value.\nWant to try again? y/n: ')
        else:
            a = 0
            user_score = 0
            computer_score = 0