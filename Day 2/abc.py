# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+i),end=" ")
#     print()

# num =0
# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+num),end=" ")
#         num+=1
#     print()

# num =0
# n=10
# for i in range(n):
#     print(" "*(n-i+1),end=" ")
#     for j in range(2*i+1):
#         print(chr(65+j),end=" ")
#         num+=1
#     print()

n=10
num =0 
for i in range(n):
    print(" "*(n-i+1),end=" ")
    for j in range(2*i+1):
        print(chr(65+j),end=" ")
        num+=1
    print()