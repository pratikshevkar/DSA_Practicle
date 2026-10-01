n = int(input("how many"))
c=0
Li = []
while(c<n):
    Li.append(int(input("enter numbers")))
    c = c+1

sum =0

for i in Li:
    sum = sum +i

print(sum)

