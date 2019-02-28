x=1
y=0
file=open("addiply.txt", "r")
number=int(file.readline(1))
y=number
lines=file.readlines()

while y > 0:
    z=lines[x]
    z=z.split()
    print(int(z[0])+int(z[1]),int(z[0])*int(z[1]))
    y-=1
    x+=1
