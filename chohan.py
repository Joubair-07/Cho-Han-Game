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
    for i in range(1, numberOfPlayers + 1):
        player = "plyer-{}".format(i)
        playersPurses[player] = initial_purse
    return playersPurses

# pot = askForPot(purse, players, player) # players[player] is the value of the key player.
def askForPot(purse, players, player):
  """Ask the player for his pot and return this value"""
  if purse > 0:
    print('You have {} DH. How much do you bet? (or QUIT)'.format(purse))
    while True: # Keep asking until the player enter a valide value. 
        pot = input('> ')
        if pot.upper().startswith('Q'):
            print('\nThanks for playing!\n{} out of the game.'.format(player))
            outPlayer(players, player)
            break
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
  else: 
    print("You Dont have purse to bet")


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
        playerWon = 1 # True <--> 1
    else :
        playerWon = 0 # False <--> 0

    return playerWon



print("One player vs The dealer    or    multiple players vs The dealer")
print("\tHow many players (1 or 2 ...)")
while True: # Keep asking until the player enter a valide vlaue.
    numberOfPlayers = input('\t> ')
    if not  numberOfPlayers.isdecimal():
        print('Please the number of players!')
        continue
    else:
        # The correct number.
        numberOfPlayers = int(numberOfPlayers)
        break


def outPlayer(players, player):
    """Make the player quit the game"""
    if players[player] != 0:
        players[player] = 0

def isPlayersExist(players):
    """Return True if all players quit the game."""
    for purse in players.values():
        if purse != 0:
            return True
    return False


# Dictionaries to store players money and changes.
playersBit = {} # Store Bits
players = {} # Stores Purses
playersPots  = {} # Stores Pots


# The main program
while True: # The game loop
    if numberOfPlayers >= 1:
        # Counting variables:
        count_dictionary_ele = 0
        number_of_out = 0
        
        if players == {}: # we dont have players yet.
            # Create a dictionary to store players with their purse.
            players = playersPurse(numberOfPlayers, purse)
        
        
        # Loop through the playersPots dictionary.
        for player, purse in players.items(): # Player is the key
            # Asks players for the pot one by one.
            print("\n",player, ": ")
            # Prompt to the player to enter his pot
            if purse != 0:
                pot = askForPot(purse, players, player) # players[player] is the value of the key player.
                # Insert the value of the pot to the dictionary playersPots.
                playersPots[player] = pot

        # Generate the value of the two dices.
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        isExist = isPlayersExist(players)
        if isExist == False:
            print("\n\n\t\t***Game Over***\n")
            sys.exit()

        print("""\nThe dealer swirls the cup and you hear rattle of dice.
The dealer slams the cup on the floor, still covering the
dice asks for your bet?""")
        # A dictionary to hold bits of players as a value.
        playersBit = {}
        # Players that won the game.
        winners = []
        # Players that lost their money.
        losers = []

        # Loop through the player to prompt for the bet.
        for player, purse in players.items():
            # Asks for the bet even(cho) or odd(han).
            if purse != 0:
                print ("\n", player, ": ")
                print('\tCHO (even) or HAN (odd)?')
                bet = askForBet()
                # Insert the bet into the playersBit dictionary.
                playersBit[player] = bet


                # Separate winners and loseres players:
                if playerWon(bet, dice1, dice2) == 1: # If the player bet is True.
                    purse += playersPots[player] # Add the the pot to the purse.
                    purse -= playersPots[player] // 10 # substruct the fee 10%.
                    players[player] = purse # insert the new purse inside the dictionary.
                    winners.append(player) # Append the winner to winners list.

                else: # the player's bet is False.
                    purse -= pot # Substruct the pot from the purse.
                    players[player] = purse # insert the new purse on the dictionary.
                    losers.append(player) # Append the loser to losers list.

        # Display results of belts
        print('\nResults :')
        print('The dealer lifts the cup to reveal:')
        print('  ', japaneseNumbers[dice1],'-', japaneseNumbers[dice2])
        print('    ', dice1, '-', dice2)
        print()

        # Loop through winners players.
        print('Winners :')
        for player in winners:
            print("\t+", player,", you won {} DH".format(playersPots[player]))
            print("\t-->The house collect a {} DH fee\n".format(playersPots[player] // 10))
        # Loop through losers .
        print('Losers :')
        for player in losers:
            print("\t+", player, ", You lost!\n")
        

        # Test if all players quit the game.
        for purse in players.values():
            count_dictionary_ele += 1
            if purse == 0:
                number_of_out += 1
        exitGame = number_of_out == count_dictionary_ele
        if exitGame:
            sys.exit()
               

