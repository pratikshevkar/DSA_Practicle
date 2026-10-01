n = int(input("how many"))
c=0
Li = []
while(c<n):
    Li.append(int(input("enter numbers")))
    c = c+1

even = 0
odd = 0

for i in Li:
    if(i%2==0):
        even = even+1
    else:
        odd = odd+1

print("count of even",even)
print("count of odd",odd)