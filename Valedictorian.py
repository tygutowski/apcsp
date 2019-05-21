anagramlist = []
num = 1
def getWords():
    num = input("How many times?")
    num = int(num)
    print("")
    for x in range(num):
        temp = input("")
        anagramlist.append(temp)
    print("")
def getAnagram():
    for x in range(len(anagramlist)):
        templist = anagramlist[x].split('|')
        if(templist[0] == templist[1]):
            print(anagramlist[x],"=","NOT AN ANAGRAM")
        elif(sorted(templist[0]) == sorted(templist[1])):
            print(anagramlist[x],"=","ANAGRAM")
        else:
            print(anagramlist[x],"=","NOT AN ANAGRAM")
getWords()
getAnagram()
