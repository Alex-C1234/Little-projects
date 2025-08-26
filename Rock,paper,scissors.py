import random

wins = 0 
losses = 0
ties = 0

choices = {1: 'rock', 2: 'paper', 3: 'scissors'}

winning_combos = {
    'rock' : 'scissors',
    'paper': 'rock',
    'scissors' : 'paper'
}

while True:

    user_input = input('Choose rock, paper or scissors (or quit) \n: ').lower()
    if user_input == 'quit':
        print('Bye Bye')
        break
    
    if user_input not in ['rock', 'paper', 'scissors']:
        print ('Nate! wtf are you doing man')
        continue

    computer_choice = choices[random.randint(1,3)]
    print(f'the computer chose: {computer_choice}')
    print(f'you chose: {user_input}')

    if user_input == computer_choice:
        print('it is a tie!')
        ties += 1

    elif winning_combos[user_input] == computer_choice:
        print('you won!')
        wins += 1
    else:
        print('you lose :(')
        losses += 1
    
    print('Wins', wins)
    print('Losses', losses)
    print('Ties', ties)

    print('---')
