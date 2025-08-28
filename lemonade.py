import random
lemons = 5
cups = 5
sugar = 5
lemonade_cups = 0
money = 10

def show_inv():
    print('-' * 30)
    print(f'Money: {money}')
    print(f'Lemonade cups: {lemonade_cups}')
    print(f'Sugar: {sugar}')
    print(f'Cups: {cups}')
    print(f'Lemons: {lemons}')
    print('-' * 30)

show_inv()

print('Welcome to your lemonade stand! Here you can buy ingredients to make lemonade and sell that to customers :) \n' )


while True:
    customer_amount = random.randint(0,5)
    usi = input('What do you want to do first? (bs, bc, bl, ml, sl, q) \n: ').lower()
    if usi == ('q'):
        break
    print('-' * 30)
    if usi == ('bs'):
        if money >= 2:
            sugar += 1 
            money -= 2
            print('Bought one bag of sugar!')
        else:
            print('Not enough money!')
    elif usi == ('bc'):
        if money >= 1:
            cups += 20
            money -= 1
            print('Bought 20 cups!')
        else:
            print('Not enough money!')
    elif usi == ('bl'):
        if money >= 1:
            lemons += 5
            money -= 1
            print('Bought 5 lemons!')
        else:
            print('Not enough money!')

    elif usi == ('ml'):
        if lemons <= 0 or cups <= 0 or sugar <= 0:
            print('Not enough resources')
        else:
            lemonade_cups += 1 
            lemons -= 1
            cups -= 1 
            sugar -= 1
            print('Made a lemonade cup!' )
    elif usi == ('sl'):
        if lemonade_cups <= 0:
            print('Not enough lemonade')
        else:
            sold = min(lemonade_cups, customer_amount)
            money += sold*2.5
            lemonade_cups -= sold
            print('Sold', sold, 'lemonade cup(s)!')
    else:
        print('Please select an action')

    show_inv()