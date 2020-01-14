# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
l=[]
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    l.append(line[20:26])
sm=0
count=0
for i in l:
    sm=sm+float(i)
    count=count+1
avg=(sm/count)
print("Average spam confidence: ",avg)
