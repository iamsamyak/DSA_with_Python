# n = int(input())
# arr = map(int, input().split())

# arr=list(arr)
# print(arr)
arr=[16, 16, 16]
n=3
x=arr[0]
for i in range(1,n-1):
    if(arr[i]>x):
        x=arr[i]
diff=x

for i in arr:
    y=x-i
    if(diff>y and y!=0):
        diff =y
        num = i
if(y==0):
         num=x
print(num)

# Another method
# c = set(arr)
# arr = list(c)
# arr = sorted(arr,reverse=True)
# print(arr[1])