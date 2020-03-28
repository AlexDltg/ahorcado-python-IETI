######################################
#   Hangman in python version beta 5 #
#     Made by Jose and Alex          #
######################################


# main function where the hangman game will be executed
def main(failures=0, turn=0, vocal="aeiou", letter=str):
    # import os for the execution of the command cls in cmd
    import os

    # Input of key word
    word = list(input("Please write a word: "))

    # clear cmd, so that the player does not know the word to guess
    os.system("cls")

    # Calculate the number of bars based on the numbers of letter of the word
    bar = list(len(word) * "_")

    # variable hangman that it will show the failures that the player has
    hangman = ['''






    =========''', '''

          |
          |
          |
          |
          |
    =========''', '''
      +---+
          |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    # main loop where the player will lose or win
    while failures != 9:

        # try, to avoid crashes
        try:
            turn += 1
            check = False
            fail = True

            # check if the turn is odd or even
            while not check:
                # If the turn is odd the player will have to write a vocal
                if turn % 2 == 0:
                    letter = input("Please write a vocal: ")
                    if letter in vocal:
                        check = True
                # If the turn is even the player will have to write a consonant
                else:
                    letter = input("Please write a consonant: ")
                    if letter not in vocal:
                        check = True

            # loop to check if the player failed or successful
            for i in range(0, len(word)):
                # if true the letter will be replace the i position of the variable bar
                if word[i] == letter:
                    bar[i] = letter
                    fail = False

            # fails count
            if fail:
                failures += 1

            # win execution
            if bar == word:
                print("Congratulations you have won!")
                break

            # print the hangman variable
            print(hangman[failures])

            # print the variable bar as string
            print(' '.join(map(str, bar)))

        except ValueError:
            print("Oops! Try it again...")


# Call the function main
main()
