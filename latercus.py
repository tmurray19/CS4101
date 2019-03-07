"""
Some pythonic testing of latercus

"""
# Hard coded from manuscripts
"""
oxford_epact = [
        19,30,11,22,3,14,25,6,17,28, 9,20,1,12,24,5,16,27,8,
        19,30,11,22,3,14,25,6,17,29,10,21,2,13,24,5,16,27,8,
        19,30,11,22,4,15,26,7,18,29,10,21,2,13,24,5,16,27,9,
        20, 1,12,23,4,15,26,7,18,29,10,21,2,14,25,6,17,28,9,
        20, 1,12,23,4,15,26,7
        ]

epact = [
        20,1,12,23,4,15,26,7,18,29,10,21,2,13,25,6,17,28, 9,
        20,1,12,23,4,15,26,7,18,30,11,22,3,14,25,6,17,28, 9,
        20,1,12,23,5,16,27,8,19,30,11,22,3,14,25,6,17,28,10,
        21,2,13,24,5,16,27,8,19,30,11,22,3,15,26,7,18,29,10,
        21,2,13,24,5,16,27,8
        ]
"""
monthEpact = [0,1,0,2,3,4,5,6,7,8,9,10]



# Dabhi paper version of latercus
year = []
index = []
easter = []

feria = [7]
# 19 for oxford
# 20 for dabhi
smart_epact = [20]


def epacter(e, idx):
    incrementer = 11
    if idx%14 == 0:
        incrementer = 12
    epact_pre = (e + incrementer)%30
    if epact_pre==0:
        epact_pre = 30
    return epact_pre


for i in range(438, 522):
    year.append(i)
    index.append(year.index(i)+1)
    if i%4==0:
        x = ((feria[-1] + 2)%7)
    else:
        x = ((feria[-1] + 1)%7)
    if x == 0:
        x = 7
    feria.append(x)
    idx = (year.index(i)+1)
    if(len(smart_epact)<84):
        smart_epact.append(epacter( (smart_epact[-1]), idx) )
"""
print(epact)
print(len(epact))

print(smart_epact)
print(len(smart_epact))
"""

"""
for i in range(len(epact)):
    if epact[i] == smart_epact[i]:
        print("OK")
    else:
        print("Not Ok")
"""

for e in range(len(smart_epact)):
    h = smart_epact[e]
    print("Epact: ", h)
    calc1 = 45-h
    print("Paschal Full Moon: ", calc1)

    y = year[e]
    print("Year: ", y)

    f = feria[e]
    feb = 28
    if y%4==0:
        feb = 29

    f = ((f+31+feb+calc1)%7)
    if f==0:
        f = 7

    if f!=7:
        calc1 += (7-f)

    print("Feria: ", f)

    if calc1 <= 25:
        alt = 74-h
        if alt > 31:
            alt = alt%31
        print("if: ", alt)

    else:
        if calc1 > 31:
            calc1 = calc1%31
        print("calc1: ", calc1)






print(feria)
print(year)
print(index)
