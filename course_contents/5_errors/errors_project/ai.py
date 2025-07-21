def interact():
    """
    Continuously prompts the user to input an integer, determines if it is even or odd, and displays the result.
    Handles invalid (non-integer) input gracefully. After each attempt, asks the user if they want to play again.
    Exits the loop and prints 'Goodbye.' if the user does not enter 'y'.
    """
    while True:  # keep looping until user reach break statement
        try:
            user_input = int(input('Please input an integer:'))     
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd')) 
        except ValueError:
            print('Please input integers only.')
        finally:
            user_input = input('Do you want to play again? (y/N):')
            if user_input != 'y':   # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit

interact()
