#!python3
list[100]=[]
length=int(input("Enter nuber of values you want to enter:"))
print("Enter numbers one by one")
for i in range(0,length):

    list[i+1]=int(input())
print(list)
