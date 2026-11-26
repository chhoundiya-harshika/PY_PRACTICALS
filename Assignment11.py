with open ("test.txt") as f:
    s= f.read()
    words=s.split()
    #print(len(words))
    
    unique_words = set(words)
    
    print("Unique words:", unique_words)
