people_filename = 'people.txt'
friends_filename = 'friends.txt'

friends_input = 'Anna, rolf, Alex, sherLok, holms , trudy, alex, charlie, maX'
friends_list = [friend.strip().lower() for friend in friends_input.strip(" ").split(',')]


with open(people_filename, 'r') as file:
    people_list = [person.strip().lower() for person in file.readlines()]

people_set = set(people_list)
friends_set = set(friends_list)
nearby_friends_list = list(friends_set.intersection(people_set))

with open(friends_filename, 'w') as file:
    for friend in nearby_friends_list:
        file.write(f'{friend.title()}\n')

try:
    with open(friends_filename, 'r') as file:
        print(f'Content of "{friends_filename}":')
        print(file.read())
except FileNotFoundError:
    print (f'File "{friends_filename}" not found.')

