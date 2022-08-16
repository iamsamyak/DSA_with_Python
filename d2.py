"""
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""




n=int(input("Enter the number"))

hash = n*2-2
star = 1

for i in range(0,n*2-1):

    for j in range(0,hash):
        print("_",end="")
    alpha = 97+n

    for k in range(hash,hash+star):
        if(k%2==0 and k>=n*2-1):
            alpha+=1
            print(chr(alpha),end="")
        elif(k%2==0):
            alpha-=1
            print(chr(alpha),end="")
        else:
            print("_",end="")

    for j in range(0,hash):
        print("_",end="")
    print()
    
    if i==n-2:
        hash=0
        star = (n*2-1)*2-1
    elif i>n-2:
        hash+=2
        star-=4
    else:
        hash-=2
        star+=4

