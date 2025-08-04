print(sum(range(2,101,2)))

even=0
for i in range(1,101):
    if i%2==0:
        even+=i
print(even)

even=0
for i in range(1,101):
    if (i&1)==0:
        even+=i
print(even)
