#Tyler Gutowski
#Is There an Echo In Here?
x=1
y=0
file=open("echo.txt", "r")
number=int(file.readline(1))
y=number
lines=file.readlines()
while y > 0:
    print(lines[x])
    print(lines[x])
    x+=1
    y-=1
