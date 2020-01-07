def swap_case(strng):
    list=[]
    for i in strng:
        if(i.isupper()):
            list.append(i.lower())
        elif(i.islower()):
            list.append(i.upper())
        else:
            list.append(i)
    fin_list=''.join(list)
    return(fin_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
