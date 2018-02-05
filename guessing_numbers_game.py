
#!/usr/bin/env python
# @filename: guessing_numbers_game.py
# @author: NullDotDEV
# @description: A simple number guessing game written purely in Python 3.6
# @last-updated: Mon Feb  5 00:12:26 -02 2018
# ===============================================================================
# HowTo: Playing this game.
# To play this game is very simple, just type:
# Example: $ python guessing_numbers_game.py


from random import randint
import requests



def main():

    # Declare and initialize variables
    use_offline_engine = False
    use_debug = False
    r_num = 0

    # Setting up variables and initializing the main flow control
    if use_offline_engine:
        r_num = randint(0, 10)
    else:
        # Make a GET http request for the random.org site API and return a random number
        req = requests.get('https://www.random.org/integers/?num=1&min=1&max=6&col=1&base=10&format=plain&rnd=new')
        r_num = int(req.text)

    if use_debug:
        print('The lenght of r_num is: %s' % len(r_num))
        print('The lenght of req.text is: %s' % len(req.text))
        print('The winning numbers were: %s' % r_num)

    user_input = int(input('Enter a number: '))

    # Print useful information for debugging purposes
    if use_debug:
        print('You entered the number: %s\n' % user_input)
        print('Type of r_num: %s' % type(r_num))
        print('Type of user_input: %s' % type(user_input))

    # Print the result to output
    # If they answered correctly
    if user_input == r_num:
        print('[ WINNER ] *** You are a winner! :)')
    # otherwise exit the program
    else:
        print('[ LOSSER ] *** You are a losser! :(')
        exit(1)


if __name__ == '__main__':
    main()

