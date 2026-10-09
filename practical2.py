#create a dict for library and print the books available or not
Library={
    101:{"Name":"JAVA_PROG"},
    102:{"Name":"PYT_PROG"},
    103:{"Name":"C++_PROG"},
    104:{"Name":"C#"},
} 

print("Lists of libraries available:")
for lid, details in Library.items():
    details["found"]=True
    if details["found"]==False:
        print(details["Name"])
    
print("No, There is no found of book")
