import random
import matplotlib.pyplot as plt

def Newline(*args):
    print(*args, end='')


def Monty_Hall(switch):
    doors = ['car', 'goat', 'goat']# List of possible prizes
    random.shuffle(doors)# will shuffle the list called doors

    
    choose = random.choice([0, 1, 2]) #randomly choose a door
    Newline('John Doe chooses door {}; '.format(choose))

    show = random.choice([x for x in [0, 1, 2] if x != choose and doors[x] == 'goat'])
    Newline('Monty shows door {} has goat; '.format(show))

    if switch:
        choose = [x for x in [0, 1, 2] if x not in [choose, show]][0]
        Newline('John Doe switches to door {}; '.format(choose))
    else:
        Newline('John Doe sticks with door {}; '.format(choose))

    Newline('door {} has {}; '.format(choose, doors[choose]))
    win = doors[choose] == 'car'
    Newline('John Doe {}!'.format('wins' if win else 'loses'))
    print()
    return win


if __name__ == '__main__':
    games = 10

    print('Test 1: Not allowed to switching')
    wins = 0
    for _ in range(games):
        if Monty_Hall(False):
            wins += 1 # If they win add 1 to "wins"
    Without_MH = wins / games
    print()

    print('test 2: Always allowed to switching')
    wins = 0
    for _ in range(games):
        if Monty_Hall(True):
            wins += 1 # If they win add 1 to "wins"
    With_MH = wins / games
    print()

    print('success rate without switching: {:.2f}'.format(Without_MH))
    print('success rate *with*  switching: {:.2f}'.format(With_MH))
   
fig = plt.figure()

fig.add_subplot(2, 2, 1)
plt.pie(Without_MH, games, labels = Monty_Hall, colors = "b")

plt.show()
 