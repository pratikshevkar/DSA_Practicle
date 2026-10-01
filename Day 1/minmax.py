n = int(input("how many"))
c=0
Li = []
while(c<n):
    Li.append(int(input("enter numbers")))
    c = c+1

min = Li[0]

sort =[]

for i in range(0,len(Li)):
    for j in range(i,len(Li)):
        if(Li[i]<Li[j]):
            temp = Li[j]
            Li[j] = Li[i]
            Li[i] = temp

for i in range(0,4):
    print(Li[i])