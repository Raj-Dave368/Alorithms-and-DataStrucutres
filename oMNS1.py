# maro mahakal

#  maro shib bhoilyo bhandaari kare mari te savari re shankar nath re re re re re shanbhunath re re re re
#  re maro bholiyo  bhatar re re re maro mabap re re maro hun 


testcases = int(input())

for i in range(testcases):
    cars = int(input())
    l = []
    for j in range(cars):
        val = int(input())
        l.append(val)
    
    minspeed = l[i]
    count = 0
    for i in l[1:]:
        if i <= minspeed:
            count += 1
        if i < minspeed:
            minspeed = i
    print(count)
