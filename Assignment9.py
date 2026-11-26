#read all lines from a file into a list. print the total number of lines and display the 2nd and 4rth line
with open ("test.txt") as f:
    s= f.readlines()
    print(s)
    print("second line:",s[1])
    print("fourth line:",s[4])
    print(len(s))