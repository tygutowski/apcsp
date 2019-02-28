#Tyler Gutowski
#Something's Missing

x=0
y=1
file=open("missing.txt", "r")
x=int(file.readline(1))
lines=file.readlines()
while x > 0:
    word = file.readline(3)
    numskip = int(lines[y][-2])
    print(lines[y][:numskip]+lines[y][numskip+1:-2])
    y+=1
    x-=1
