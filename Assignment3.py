#accept the name and check if its palindrome
num=int(input("Enter a num:"))
temp = num
rev = 0
while num>0:
    n=num%10
    rev=rev*10+n
    num=num//10
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")