n = int(input("how many"))
c=0
Li = []
while(c<n):
    Li.append(int(input("enter numbers")))
    c = c+1

se = int(input("enter element to search"))

flag = 1
for i in range(0,len(Li)):
    if Li[i]==se:
        flag = 0
        po = i

if flag == 0:
    print(f"{se} is present at{po+1}")
else:
    print(f"{se} is not present")