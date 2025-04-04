import random
import ascii_art

ascii_art.title()

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display = []
word_length = len(chosen_word)
lives=6
for _ in range(word_length):
    display += "_"
end_of_game=False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if '_' not in display:
        print("You win.")
        end_of_game=True
    if guess not in chosen_word:
        print(ascii_art.stages[lives])
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose.")
