# try:
#     a=10
#     b=0
#     result=a/b
#     print(result)
# except:
#     print("There is a ZeroDivisionError Please solve it!")
# print("Program completed")


# print("Hello everyone ")
# print("Today We are practicing exception handling")
# try:
#     num=int(input("enter a number:"))
#     result=100//num
#     print("Result", result)
# # except ValueError:
# #     print("Please enter a valid numver")
# # except ZeroDivisionError:
# #     print("You cannot divide by zero")
# # else:
# #     print("program executed successfully!")
# finally:
#     # print("it will run in any condition")
#     print("it must be executed")

# age =15
# try:
#     if age <18:
#         raise ValueError("not eligible")
# except ValueError as e:
#     print("ValueError:", e)
# else:
#     print("Access granted")

class MyException(Exception):
    pass
age = 15
try:
      if age <18:
        raise MyException("not eligible")
# except MyException as e:
    # print("Error:", e)
# else:
#     print("Access granted")
finally:
    print("Program executed successfully")