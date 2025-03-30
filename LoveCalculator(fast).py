print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

def true(char:chr)->bool:
    if char=='t' or char=='r' or char=='u' or char=='e':
        return True
    return False
def Love(char:chr)->bool:
    if char=='l' or char=='o' or char=='v' or char=='e':
        return True
    return False

cnt=0
name=(name1+name2).lower()
for x in name:
    if true(x):
        cnt+=1
print("Love: ",end="")        
print(cnt,end="")
cnt=0     
for x in name:
    if Love(x):
        cnt+=1
print(cnt,'%')  
