import random
# from hangman_art import logo,stages --> or we ca write it like this
import hangman_art
import os
# Word bank of animals
'stork swan tiger toad trout turkey turtle weasel whale wolf '
words_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
              'coyote crow deer dog donkey duck eagle ferret fox frog goat '
              'goose hawk lion lizard llama mole monkey moose mouse mule newt '
              'otter owl panda parrot pigeon python rabbit ram rat raven '
              'rhino salmon seal shark sheep skunk sloth snake spider '
              'wombat zebra ').split()
print(hangman_art.logo)
word = (random.choice(words_list)).lower()
ans = []
for i in range(0, len(word)):
    ans += "_"
print(ans)
i = 0
end_of_game = False

while not end_of_game:
    letter = input("Guess a letter: ")
    os.system("cls")
    counter = False
    for pos in range(len(word)):
        if word[pos] == letter:
            counter = True
            if ans[pos] == "_":
                ans[pos] = letter
            else:
                print("You have aready entered the letter ", letter)
    print(ans)
    if not counter:
        i += 1
        print("You entered a wrong letter")
        if i > 5:
            print("You Lost")
            end_of_game = True
    print(hangman_art.stages[i])
    if "_" not in ans:
        end_of_game = True
        print("You Win!!!!!")
