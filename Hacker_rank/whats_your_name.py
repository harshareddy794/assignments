def print_full_name(a, b):
    string="Hello "+a+" "+b+"! You just delved into python"
    return(string)
if __name__ == '__main__':                   #Hello firstname lastname! You just delved into python.
    a=input()
    b=input()
    string=print_full_name(a,b)
    print(string)
