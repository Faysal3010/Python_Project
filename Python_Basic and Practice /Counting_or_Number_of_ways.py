n=int(input("Total Posibility: "))
m=int(input("Number of value: "))
mem=[0]*(n+1)
mem[0]=1

for i in range(1,n+1):
    mem[i]=sum(mem[max(0,i-m):i])

print(mem[n])
