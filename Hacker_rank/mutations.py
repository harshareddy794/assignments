def mutate_string(string, position, character):
    lis=list(string)
    lis[position]=character
    lis=''.join(lis)
    return(lis)

if __name__ == '__main__':
    string=input()
    position=int(input())
    character=input()
    output=mutate_string(string,position,character)
    print(output)
