n = int(input("how many"))
c=0
Li = []
while(c<n):
    Li.append(int(input("enter numbers")))
    c = c+1
new =[]
for i in Li:
    if i not in new:
        new.append(i)

print(new)
