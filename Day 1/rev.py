n = int(input("how many"))
c=0
Li = []
while(c<n):
    Li.append(int(input("enter numbers")))
    c = c+1

rev = []

for i in range((n-1),-1,-1):
    rev.append(Li[i])
print(rev)
