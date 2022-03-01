def countwords():
    fname = input("enter your file name : ")
    numberofwords = 0
    file = open(fname, "r")
    for i in file :
        words = i.split()
        numberofwords =  numberofwords + len(words)
    print(numberofwords)
countwords()