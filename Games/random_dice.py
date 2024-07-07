import random

dice = input("Number of sides: ")

if dice.isdigit():
    top_of_range = int(dice)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(1, top_of_range)

print("The drawn number is:", random_number)

# ------

'''
Melhorias:
- Adicionar interface gráfica
'''