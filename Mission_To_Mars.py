dist = float(0)
speed = float(0)

with open("Prob08.in.txt") as file:
    for line in file:
        for ch in range(len(line)):
            if line[ch] == " ":
                dist = float(line[:ch])
                speed = float(line[ch:])
                break
        if dist > 0 and speed > 0:
            totalhours = (dist * 1000000)/speed
            
            days = totalhours/24
            print("Time to Mars:",int(days),"days, ",end='')
            
            hours = (days - int(days)) * 24
            print(int(hours),"hours, ",end='')
            
            minutes = (hours - int(hours)) * 60
            print(int(minutes),"minutes, ",end='')
            seconds = (minutes - int(minutes)) * 60
            print(int(seconds),"seconds")
