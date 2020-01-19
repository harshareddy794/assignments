if __name__ == '__main__':
    lis=[]
    n = int(input())
    for i in range(0,n):
        inp=(input()).split()
        if inp[0]=='insert':
            lis.insert(int(inp[1]),int(inp[2]))
        if inp[0]=='print':
            print(lis)
        if inp[0]=='remove':
            lis.remove(int(inp[1]))
        if inp[0]=='append':
            lis.append(int(inp[1]))
        if inp[0]=='sort':
            lis.sort()
        if inp[0]=='pop':
            lis.pop()
        if inp[0]=='reverse':
            lis.reverse()
