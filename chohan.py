""" Cho-Han by joubair alphajoubair04@gmail.com
The traditional Japanese dice game of even-odd.
"""

# Import modules:
from random import randint
import sys

# Nubmers in japense language:
japaneseNumbers = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                   4: 'SHI', 5: 'GO', 6: 'ROKU'}

# The player Start with this much of money
purse = 5000 # DH

# Intro for the Game.
print('''Cho-Han By alphajoubair04@gmail.com

In this traditional dice game, two dice are rolled in bumbo
cup by the dealer setting in the floor. The player must guess
the total of two dices is even (CHO) or odd (HAN) number.
''')

def playersPurse(numberOfPlayers, initial_purse):
    """Generate a dictionary containing the intial value 
    for each player."""
    playersPurses = {}
    for i in range(numberOfPlayers):
        player = "plyer-{}".format(i)
        playersPurses[player] = initial_purse
    return playersPurses

def askForPot(purse):
    """Ask the player for his pot and return this value"""
    print('You have {} DH. How much do you bet? (or QUIT)'.format(purse))
    while True: # Keep asking until the player enter a valide value. 
        pot = input('> ')
        if pot.upper().startswith('Q'):
            print('\nThanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('\nPlease enter a number!')
            continue
        elif int(pot) > purse:
            print('\nPlease enter a value between 1 and {}'.format(purse))
            continue
        else: # The correct value.
            pot = int(pot) # Convert a string to an integre.
            break
    return pot


def askForBet():
    """Asks the player to enter a bit and return
    the value of the bit."""
    
    while True: # keep asking until they insert (CHO) or (HAN).
        bet = input('> ').upper()
        if bet not in ('CHO', 'HAN'):
            print('Please enter ether (CHO) or (HAN).')
            continue
        else:
            break
    return bet

def playerWon(bet, dice1, dice2):
    """Return True if the player won and return 
    False in the other hand"""
    
    # Determine if the total of the dices is even (CHO).
    rollIsEven = (dice1 + dice2) % 2 == 0

    # Determine the correct bet.
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    # Determine if the player won.
    if correctBet == bet:
        playerWon = 1
    else :
        playerWon = 0

    return playerWon




print("One player vs The dealer    or    multiple players vs dealer")
print("\t(1 or 2 or 3 ...)")
numberOfPlayers = input('\t> ')
while True:
    if not  numberOfPlayers.isdecimal():
        print('Please a number (1 or more)')
        continue
    else:
        numberOfPlayers = int(numberOfPlayers)
        break

while True: # The game loop
    if numberOfPlayers > 1:
        players = playersPurse(numberOfPlayers, purse)
        playersPots = {}
        for player in players.keys():
            print("\n",player, ": ")
            pot = askForPot(players[player])
            playersPots[player] = pot

        # Generate the value of the two dices.
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        print("""\nThe dealer swirls the cup and you hear rattle of dice.
The dealer slams the cup on the floor, still covering the
dice asks for your bet?""")
        playersBit = {}
        wonPlayers = []
        lostPlayers = []
        for player in players.keys():
            print ("\n", player, ": ")
            print('\tCHO (even) or HAN (odd)?')
            bet = askForBet()
            playersBit[player] = bet


            if playerWon(bet, dice1, dice2) == 1:
                purse += playersPots[player]
                purse -= playersPots[player] // 10
                players[player] = purse
                wonPlayers.append(player)
            else:
                purse -= pot
                lostPlayers.append(player)

        # Display results of belts
        print('\nResults :')
        print('The dealer lifts the cup to reveal:')
        print('  ', japaneseNumbers[dice1],'-', japaneseNumbers[dice2])
        print('    ', dice1, '-', dice2)
        print()

        for player in wonPlayers:
            print(player,", you won {} DH".format(playersPots[player]))
            print("The house collect a {} DH fee\n".format(playersPots[player] // 10))
        for player in lostPlayers:
            print(player, ", You lost!\n")
                





    # check if the palyer run out of money.
    for player in players.keys():
      if players[player] <= 0:
          del players[player]

    # If all players lost their money
    if players == {}:
        sys.exit()


