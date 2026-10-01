n = int(input("how many"))
c=0
Li = []
while(c<n):
    Li.append(int(input("enter numbers")))
    c = c+1
zero = 0
ele =0
new =[]
for i in Li:
    if i!=0:
        new.append(i)
        ele = ele+1
    else:
        zero = zero+1

sum = (ele+zero)
for i in range(ele,sum):
    new.append(0)
print(new)