import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(''' 
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  ;
| |          ||  `/,|
| |          (\`_.'
| |         .-`--'.
| |        /Y . . Y.
| |       // |   | ||
| |      //  | . |  ;;
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
      ''')
words=["apple","banana","egg","fish"]
word=random.choice(words)
print(word)
index=[]
dead=0
ok=False
for _ in range(len(word)):
    index.append('_')
while True:
    guess_a_letter=(input("Guess a letter: "))
    print("".join(index))
    found= False
    for i in range(0,len(word)):
      if guess_a_letter==word[i]:
        index[i]=guess_a_letter
        found=True
    if found==False:
        print(f"'{guess_a_letter}' is not found this is word")
        dead+=1
        ok=True
    if ok:
        print(HANGMANPICS[dead])
    print("".join(index))
    if "".join(index)==word:
        print("You won")
        break
    if dead==7:
       print("You lose this game!!")
       break

