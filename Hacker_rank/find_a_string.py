import string
count=0
if __name__ == '__main__':
    string=input()
    sub_string=input()
    for i in range(0,len(string)):
        if(string[i:i+len(sub_string)]==sub_string):
                count=count+1
print(count)
