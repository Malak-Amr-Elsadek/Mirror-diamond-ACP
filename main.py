row=int(input("Enter a number:"))

for i in range(1,row+1):
    for j in range(i,row):
        print(" ",end=" ")

    for k in range(1,i+1):
        print(k,end=" ")

    print()