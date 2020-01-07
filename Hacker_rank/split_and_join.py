#!python3
def split_and_join(string):
    string=string.split(" ")
    string='-'.join(string)
    return(string)

if __name__ == '__main__':
    string=input("Enter string:")
    final_string=split_and_join(string)
    print(final_string)
