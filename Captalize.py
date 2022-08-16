
"""
s="samyak Jain"
s=s.split(" ")
i=0
for i in range(0,len(s)):
    small = ord(s[i][0])
    if (97<= small and small <=122):
        s[i]=chr(small-32)+ s[i][1:]
    
t=""
for i in s:
    t=t+i+" "
print(t)
"""
s = "12samyak is  good  "

small = ord(s[0])
if (97<= small and small <=122):
    t = chr(small-32)
    s = t+s[1:]

for i in range(0,len(s)-1):
    try:
        if(s[i]==" "):
            small = ord(s[i+1])
            if (97<= small and small <=122):
                t = chr(small-32)
                s= s[:i+1]+t+s[i+2:]
    except:
        print("error")
print(s)