import random 

usi = int(input('How many times do you want to flip this coin?\n'))
heads = 0
tails = 0

for i in range(usi): 
    if random.randint(1,2) == 1:
        print('Tails!')
        tails += 1
    else:
        print('Heads')
        heads += 1

print(f'Results:\n Heads: {heads}\n Tails: {tails}')