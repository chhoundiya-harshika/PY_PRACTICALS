# try:
#     a=10
#     b=0
#     result=a/b
#     print(result)
# except:
#     print("There is a ZeroDivisionError Please solve it!")
# print("Program completed")

try:
    num=int(input("enter a number:"))
    result=100/num
    print("Result", result)
except ValueError:
    print("Please enter a valid numver")
except ZeroDivisionError:
    print("Yo cannot divide by zero")
        