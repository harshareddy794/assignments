fname = input("Enter file name: ")
fh = open(fname)
lst = list()
l=list()
for line in fh:
	string=(line.rstrip()).split()
	for i in range(0,len(string)):
		l.append(string[i])
l.sort()
for i in l:
	if i in lst:
		continue
	else:
		lst.append(i)
print(lst)
