import random
import string

print('Welcome to the Password Picker\n')
while True:
    for num in range(5):
        adjectives = ['drowsy', 'horny', 'fluffy', 'chunky', 'funky',
                      'handsome', 'beautiful', 'smelly', 'tall', 'sloopy',
                      'short', 'stinky']

        nouns = ['people', 'cars', 'goats', 'elephants', 'cheeseburgers',
                 'frats', 'dogs', 'hotdogs', 'sharks', 'jackets']



        adjectives = random.choice(adjectives)
        nouns = random.choice(nouns)
        numbers = random.randrange(0, 70)
        special_char = random.choice(string.punctuation)

        password = adjectives + special_char + str(numbers) + nouns + special_char

        print(f'Your new password is: {password}')

    response = input('Would you like another password? Type y/n')
    if response == 'n':
        break

