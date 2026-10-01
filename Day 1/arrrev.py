n = int(input("how many"))
c=0
Li = []
while(c<n):
    Li.append(int(input("enter numbers")))
    c = c+1

nel = Li[::-1]

print(nel)