#!python3
list=[]
length=int(input("Enter nuber of values you want to enter:"))
print("Enter numbers one by one:")
for i in range(0,length):
    list.append(int(input()))
list.sort()
runner=list[-2]
print("\nScore of runner is: ",runner)
