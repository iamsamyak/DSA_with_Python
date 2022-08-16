
x= "www.AmaZon.Com"
t=""
for i in x:
    Ascii = ord(i)
    if (65<= Ascii <=90):
        t+= chr(Ascii+32)
        

    elif(97<=Ascii <=122):
        t+= chr(Ascii-32)
    
    else:
        t+=i

print(t)


