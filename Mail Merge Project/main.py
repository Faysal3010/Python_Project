#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.docx") as file:
    starting_letter=file.read()
with open("Input/Names/invited_names.txt") as file:
    invited_names=file.readlines()
length=len(invited_names)

for i in range(length):
    new_contents=starting_letter.replace("[name]",invited_names[i][:-1])
    with open(f"Output/ReadyToSend/{invited_names[i][:-1]}.docx",mode='w') as file:
        file.write(new_contents)
