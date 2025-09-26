def guessing_game():
    # TODO create guessing game function
    # HINT: Target number should be 15
    # HINT: Return message should be "Congratulations! You guessed it!"
    # HINT: Use input("Enter your guess: ") for user input
    # HINT: Print "Too low! Try again." for low guesses
    # HINT: Print "Too high! Try again." for high guesses
    while():
        num = int(input("Enter your guess: "))
        if(num==15):
            print("Congratulations! You guessed it!")
        elif(num>15):
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")


if __name__ == "__main__":
    # create guessing game below this
    pass
