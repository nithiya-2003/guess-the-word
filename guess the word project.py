import random

animals = ['elephant', 'bear', 'cheetah', 'giraffe', 'wolf', 'tiger', 'penguin',
           'rabbit', 'lion', 'monkey', 'rhinoceros', 'sheep', 'kangaroo', 'zebra']
fruits = ['apple', 'banana', 'grapes', 'mango', 'lime', 'watermelon', 'jackfruit',
          'guava', 'orange', 'papaya', 'pear', 'peach', 'pomegranate', 'strawberry']
stationery = ['pencil', 'eraser', 'sharpener', 'envelope', 'paper', 'stapler', 'folder',
              'marker', 'inkpot', 'calculator', 'glue', 'notebook', 'scissors', 'ruler']

while True:
    words = animals + fruits + stationery
    random_word = random.choice(words)

    if random_word in animals:
        print("Hint: It is an animal.")
    elif random_word in fruits:
        print("Hint: It is a fruit.")
    else:
        print("Hint: It is a stationery item.")

    guessed_letters = ""
    chances = 5

    while chances > 0:
        wrong_guesses = 0
        for letter in random_word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                wrong_guesses += 1
                print("_", end=' ')

        print()

        if wrong_guesses == 0:
            print(f"Congrats! You won. The word is {random_word}.")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == "y":
                break
            else:
                print("THANKS FOR PLAYING...")
                quit()

        guess = input("Make a guess: ").lower()
        guessed_letters += guess

        if guess not in random_word:
            chances -= 1
            print(f"Wrong. You have {chances} more chances.")
            if chances == 0:
                print(f"Game over. You lose. The word was {random_word}.")
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again == "y":
                    break
                else:
                    print("THANKS FOR PLAYING...")
                    quit()
