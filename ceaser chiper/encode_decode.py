
def encode():
    message=input("Type your message: ").lower()
    shift_number=int(input("Type the shift number: "))
    print("Here's the encoded result: ",end="")
    for letter in message:
        x = (ord(letter)-97) + shift_number
        if x> 25:
          x = x % 25
        print(chr(x+97),end="") 

def decode():
    message=input("Type your message: ").lower()
    shift_number=int(input("Type the shift number: "))
    print("Here's the encoded result: ",end="")
    for letter in message:
        x = (ord(letter)-97) - shift_number
        if x < 0:
          x = x % 25
        print(chr(x+97),end="")

type=ok=True
while type:
        
        transform=input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        if transform=='encode': 
         encode()
        elif transform=='decode':
         decode()
        print()
        type=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if type=='yes':type=True
        elif type=='no':type=False
