#write a program to read a file and count how many vowels are present in its content
with open ("test.txt") as f:
    s= f.read()
    str="aeiouAEIOU"
    vowel_count=0
    consonet_count=0
    for i in s:
        for chr in i:
            if chr.isalpha():
                if i in "aeiouAEIOU":
                    vowel_count+=1
                else:
                    consonet_count+=1
                    
    print("vowels_count:", vowel_count)
    print("consonet_count:", consonet_count)
         
        