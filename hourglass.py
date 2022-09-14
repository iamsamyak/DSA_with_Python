a=0;b=0;n=6;sum=0
arr= [[-9 ,-9, -9,  1, 1, 1 ],[0, -9,  0,  4, 3 ,2],[-9, -9, -9,  1, 2, 3],[0,  0,  8,  6, 6, 0],[0,  0,  0, -2, 0, 0],[0,  0,  1,  2, 4, 0]]
c=1
sum1=-99999
while(a!=n-2):
    sum=0
    for i in range(a,a+3):
        for j in range(b,b+3):
            if(c!=4 and c!=6):
                sum += arr[i][j]
            c+=1    

    if sum>sum1:
        sum1=sum
    c=1
    if(n-3 == b):
        a+=1
        b=0
    else:
        b+=1



print(sum1)

