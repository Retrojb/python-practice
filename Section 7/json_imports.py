import json

with open('friends_json.txt', 'r') as file:  #contents manager auto open and close at the end of the block
    file_contents = json.load(file)  #Converts a json to a dictionary

print(file_contents['friends'][0])


cars = [
    {'make': 'Chevy', 'model': 'nova'},
    {'make': 'Dodge', 'model': 'challenger'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)

