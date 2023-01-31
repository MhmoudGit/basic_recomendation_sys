import random

list = [
    ['naruto', 'action', 'long'],
    ['detective conan', 'mystery', 'long'],
    ['gundam wings', 'action', 'short'],
    ['street fighter', 'action', 'short'],
    ['one piece', 'adventure', 'long']
]

print('whats ur mood?')
mood = input()
duration = input()
for i in list :
    if i[1] == mood and i[2] == duration:
        choice = i[0]
        print(choice)
    if i[1] == mood and i[0] != choice:
        recomendations = i[0]
        print('another recomendations: ',recomendations)



