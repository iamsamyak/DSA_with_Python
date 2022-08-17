n = int(input("enter value of n"))
m = n*3
x = (m/2)-2 if m%2==0 else (m+1)/2-2
for i in range(n):

    if(int(n/2) != i):
        print("-"*int(x),end="")
        temp = m-(x*2)
        print(".|."* int(temp//3),end="")
        print("-"*int(x),end="")
        if int(n/2) < i:
            x+=3
        else:
            x-=3
    
    else:
        v = (m-7)/2
        print("-"*int(v),end="")
        print("WELCOME",end="")
        print("-"*int(v),end="")
        x=3
    print()