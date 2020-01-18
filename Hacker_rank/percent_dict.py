data=dict()
students=int(input())
for i in range(0,students):
    name=input().split()
    marks=[]
    for i in range(1,4):
        marks.append(int(name[i]))
    data[name[0]]=marks
key=input()
sum=0
for i in data[key]:
    sum=sum+i
print(sum/3)
