import random

Wins = 0
wrong_guesses = 0

while True:
    cc = random.randint(1,100)
    user_input =(input('Guess a number between 1 and 100 (exit to quit) \n: '))

    while True: 

        if user_input.lower() == 'quit':
            print('Game over! the number was: ', cc)
            print('Wins: ', Wins)
            print('Wrong guesses: ', wrong_guesses)
            exit()

        try:
            guess = int(user_input)
        except ValueError:
            print('Please use a number or quit')
            user_input = input('Try again \n:')
            continue

        if guess > cc:
            print('You guessed too high!')
            wrong_guesses += 1
        elif guess < cc:
            print('you guessed too low!')
            wrong_guesses += 1
        else:
            print('You won!')
            Wins += 1
            print('Wins: ', Wins)
            print('Wrong guesses: ', wrong_guesses)
            break
        
        user_input =(input('Try again! (or quit) \n: '))   