import array

def reverseArray(a):
    # Write your code here
    l = len(a)
    na=array.array('I',())
    for i in range(l-1,-1,-1):
        na.append(a[i])
        
    return na



a= [1,2,3,4]
print(reverseArray(a))