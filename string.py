s= "samyak"
t=s
print(id(s)==id(t))
# you can see that the python to reduce the space it resuses the same obejct
pos = 3
char = "I"
print(s[0:pos-1]+char+s[pos:]) 

