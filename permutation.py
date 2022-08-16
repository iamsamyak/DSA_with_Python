# Python function to print permutations of a given list
x,y,z,n=1,1,1,2


x_list = [i for i in range(0,x+1)]
y_list = [i for i in range(0,y+1)]
z_list = [i for i in range(0,z+1)]

l = []
for i in x_list:
    for j in y_list:
        for k in z_list:
            l.append([i,j,k])
s=[]
sum=0
for i in l:
    for j in i:
        sum+=j
    if sum!=n:
        s.append(i)
    sum=0

print(s) 