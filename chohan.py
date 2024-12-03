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


while True: # The game loop.

    print('You have {} DH. How much do you bet? (or QUIT)'.format(purse))
    while True: # Keep asking until the player enter a valide value. 
        pot = input('> ')
        if pot.upper().startswith('Q'):
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number!')
            continue
        elif int(pot) > purse:
            print('Please enter a value between 1 and {}'.format(purse))
            continue
        else: # The correct value.
            pot = int(pot) # Convert a string to an integre.
            break

    # Generate the value of the two dices.
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)

    print("""The dealer swirls the cup and u hear rattle of dice.
The dealer slams the cup on the floor, still covering the
dice asks for your bet?""")
    print()
    print('\tCHO (even) or HAN (odd)?')

    while True: # keep asking until they insert (CHO) or (HAN).
          bet = input('> ').upper()
          if bet not in ('CHO', 'HAN'):
              print('Please enter ether (CHO) or (HAN).')
              continue
          else:
              break
          

    # Determine if the total of the dices is even (CHO).
    rollIsEven = (dice1 + dice2) % 2 == 0

    # Determine the correct bet.
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'


    # Determine if the player won.
    playerWon = correctBet == bet

    print('The dealer lifts the cup to reveal:')
    print('  ', japaneseNumbers[dice1],'-', japaneseNumbers[dice2])
    print('    ', dice1, '-', dice2)

    # Display the bet resutls.
    # If the playerWon = True:
    if playerWon:
        print('You won! You take {} DH'.format(pot))
        print(f"The house collects a {pot // 10} DH fee.")
        purse += pot  # Add the pot the palyer's purse.
        purse -= pot // 10 # The house take 10% fee.

    # Else the playerWon = False:
    else:
        print('You lost!')
        purse -= pot # The house take your pot.

    # check if the palyer run out of money.
    if purse <= 0:
        print()
        print('You lost all your money')
        print('Tanks for playing')
        sys.exit()




    

     

    
