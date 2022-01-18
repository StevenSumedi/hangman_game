import hangman_images, words, random

print("Hangman")
print("\nInstructions: Identify the mystery word. Do so by guessing one letter at a time or by guessing the whole word at once.\nJust be sure to identify the word before our hangman gets hung!\n")

while True:
    print("There are 4 categories of words to choose from, plus one extra hard word if you're feeling adventurous.")
    print("1. Short (6-7 letters)")
    print("2. Medium (8-9 letters)")
    print("3. Long (10+ letters)")
    print("4. Extra hard challenge word, according to science\n")

    while True:
        difficulty = input("Select a difficulty: ")

        if difficulty == "1":
            word = random.choice(list(words.words_6ltrs))
            break
        elif difficulty == "2":
            word = random.choice(list(words.words_8ltrs))
            break
        elif difficulty == "3":
            word = random.choice(list(words.words_10ltrs))
            break
        elif difficulty == "4":
            word = words.hardest_word
            break

    word = word.upper()
    word_length = len(word)
    underscored_word = list(word_length * '_')
    letters_remaining = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print(f"\n{underscored_word}")

    won_game = False
    lives = 7
    dict_index = 0
    while won_game == False and lives != 0:
        guess = input("Guess the word or a single letter: ")
        guess = guess.upper()
        guess_length = len(guess)

        if guess == word:
            won_game = True
            underscored_word = word
            print(list(word))
            continue
        elif guess_length == 1 and guess in word and guess not in str(underscored_word):
            index = 0
            for letter in word:
                if guess == letter and index < (word_length):
                    underscored_word[index] = letter
                    index += 1
                    if underscored_word == list(word):
                        won_game = True
                        break
                else:
                    index += 1
            index = 0
            print(f"\n{underscored_word}")
            letters_remaining.remove(str(guess.upper()))
            if won_game == False:
                print("\nLetters remaining:", *letters_remaining)
            continue
        else:
            lives -= 1
            dict_index += 1
            if len(guess) == 1 and guess in letters_remaining:
                letters_remaining.remove(str(guess.upper()))
            print(f"\n{hangman_images.hangman[dict_index]}")
            print(underscored_word)
            if lives != 0:
                print("\nLetters remaining:", *letters_remaining)

    if won_game == True:
        print("\nCongratulations, you win! Do a happy dance!")
    else:
        print(f"\nSorry, you lose. The word was: {word}.")

    while True:
        again = input("\nWould you like to play again (y or n)? ")
        if again.lower() == "y":
            print("\n")
            break
        elif again.lower() == "n":
            exit()
