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
| |       // |   | ;;
| |      //  | . |  ;;
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | ;
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
      

888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"    


      ''')
words=["apple","banana","egg","fish"]
word=random.choice(words)
print(word)
index=[]
dead=0
ok=False
for _ in range(len(word)):
    index.append('_')
while dead<7:
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
     if dead>=0 and dead<=6:
        print(HANGMANPICS[dead])
    print("".join(index))
    if "".join(index)==word:
        print("You won")
        break

if dead==7: print("You lose!!")
