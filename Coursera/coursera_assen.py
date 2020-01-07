import string
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find("0")
slice=text[pos+1:pos+6]
num=float(slice)
print(num)
