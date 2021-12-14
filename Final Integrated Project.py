# Creator David Ritchie

# COP 1500

# Details of Program:  Runs a Choose Your Own Adventure game, forcing you to choose a weapon, and
# then running you through a series of other choices.

# Website that helped me:the coding pie.com which had a good details on making small games like this

import time

# Variable that decides whether the game will run again or not.
goOn = True

# Variables that store how many wins and loses you get.
wins = 0
loses = 0


# Displays a message when you win
def win():
    print('{:*^80}'.format(''))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('You won, Good Job.'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))


# Displays a message when you lose
def lose():
    print('{:*^80}'.format(''))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('Dang. You lost.'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))


# Return T or F for Y or N (to be used to reassign goOn var).
def cont(yn):
    if yn == 'y':
        return True
    elif yn == 'n':
        return False


# Main program. runs the Choose Your Own Adventure game.

while goOn:
    print("Pick your Weapon.")
    time.sleep(1)
    # Decide between sword and wand
    # while choice == (not ('sword' or 'wand')):
    choice = input('Sword or wand? ').lower()
    if choice == 'sword':
        weapon = 'sword'
        # Decide between left or right.
        print("Good choice! Now what monster do you want to kill?")
        time.sleep(1)
        choice = input('Ogre or Beast? ').lower()
        if choice == 'ogre':
            print("You've reached the swamp!")
            time.sleep(1)
            choice = input('Left or Right? ').lower()

            if choice == 'left':
                print('{}'.format("You come up on a little hut in the middle of the swamp."))
                time.sleep(3)
                print('{}'.format("Suddenly, you hear footsteps behind you."))
                time.sleep(3)
                print('{}'.format("Startled, you turn around, and then hear:"))
                time.sleep(3)
                time.sleep(3)
                win()
                wins += 1
            elif choice == 'right':
                print('Oh no! An Ogre!')
                time.sleep(1)
                if weapon == 'sword':
                    print('You slice the Ogre.')
                    time.sleep(1)
                    win()
                    wins += 1
                elif weapon != 'sword':
                    print('The Ogre breaks your wand, and then you.')
                    time.sleep(1)
                    lose()
                    loses += 1
                else:
                    print('Pick a valid input!')
        # Decide between dunes or canyon.
        elif choice == 'beast':
            print("You've reached the desert!")
            time.sleep(1)
            choice = input('Dunes or canyon? ').lower()

            if choice == 'dunes':
                print("You stumble upon the Beast!")
                time.sleep(1)
                if weapon == 'sword':
                    print('The Beast eats your sword, and then you.')
                    time.sleep(1)
                    lose()
                    loses += 1
                elif weapon == 'wand':
                    print('You cast a mighty fireball at the Beast!')
                    time.sleep(1)
                    win()
                    wins += 1
                else:
                    print('Pick a valid input!')

            elif choice == 'canyon':
                print('You find a witch\'s hut. She invites you in.')
                time.sleep(1)
                choice = input('Go in or leave? ').lower()

                if choice == 'go in':
                    print('She casts a dark spell, puts you in a coma, and then cooks you and eats you.')
                    time.sleep(1)
                    lose()
                    loses += 1
                elif choice == 'leave':
                    print('You leave her hut and stumble around a bit in the desert, eventually dying of starvation.')
                    time.sleep(1)
                    lose()
                    loses += 1
                else:
                    print('Pick a valid input!')
            else:
                print('Pick a valid input!')
        else:
            print('Pick a valid input!')

    elif choice == 'wand':
        weapon = 'wand'
        print("Good choice! What place do you want to go now?")
        time.sleep(1)
        choice = input('Swamp or Desert? ').lower()

        if choice == 'swamp':
            print("You've reached the swamp!")
            time.sleep(1)
            choice = input('Left or Right? ').lower()

            if choice == 'left':
                print('{}'.format("You come up on a little hut in the middle of the swamp."))
                time.sleep(3)
                print('{}'.format("Suddenly, you hear footsteps behind you."))
                time.sleep(3)
                print('{}'.format("Startled, you turn around, and then hear:"))
                time.sleep(3)
                time.sleep(3)
                win()
                wins += 1
            elif choice == 'right':
                print('Oh no! An Ogre!')
                time.sleep(1)
                if weapon == 'sword':
                    print('You slice the Ogre.')
                    time.sleep(1)
                    win()
                    wins += 1
                elif weapon != 'sword':
                    print('The Ogre breaks your wand, and then you.')
                    time.sleep(1)
                    lose()
                    loses += 1
                else:
                    print('Pick a valid input!')
            else:
                print('Pick a valid input!')

        elif choice == 'desert':
            print("You've reached the desert!")
            time.sleep(1)
            choice = input('Dunes or canyon? ').lower()

            if choice == 'dunes':
                print("You stumble upon the Beast!")
                time.sleep(1)
                if weapon == 'sword':
                    print('The Beast eats your sword, and then you.')
                    time.sleep(1)
                    lose()
                    loses += 1
                elif weapon == 'wand':
                    print('You cast a mighty fireball at the Beast!')
                    time.sleep(1)
                    win()
                    wins += 1
                else:
                    print('Pick a valid input!')

            elif choice == 'canyon':
                print('You find a witch\'s hut. She invites you in.')
                time.sleep(1)

                choice = input('Go in or leave? ').lower()
                if choice == 'go in':
                    print('She casts a dark spell, puts you in a coma, and then cooks you and eats you.')
                    time.sleep(1)
                    lose()
                    loses += 1
                elif choice == 'leave':
                    print('You leave her hut and stumble around a bit in the desert,eventually dying of starvation.')
                    time.sleep(1)
                    lose()
                    loses += 1
                else:
                    print('Pick a valid input!')
            else:
                print('Pick a valid input!')
        else:
            print('Pick a valid input!')

    else:
        print('Pick sword or wand next time!')
    time.sleep(3)
    print('You have won {} times.'.format(wins))
    print('You have lost {} times.'.format(loses))
    time.sleep(2)
    decision = input('Do you want to play again? y/n \n')
    goOn = cont(decision)
