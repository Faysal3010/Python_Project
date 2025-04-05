alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift,direction):
    end_text=""
    if direction=="decode":
        shift*=-1
    for letter in text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position+shift)%26
            end_text+=alphabet[new_position]
        else: end_text+=letter
    print(f"Here {direction}d is: {end_text}")

should_end=True
while should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text,shift,direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = False
    print("Goodbye")
