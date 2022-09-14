n = 1234
rev=0

while n!=0:
    rem = n%10
    rev = rev*10 + rem
    n/=10

if n==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")