"""
Some pythonic testing of latercus
http://adsbit.harvard.edu//full/1993JHA....24..204M/0000204.000.html


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

def marchEpact(e, year):
    feb = 28
    if y%4==0:
        feb = 29
    e = e + 31 + feb
    print("e: ", e)
    march_epact = e%30
    if march_epact==0:
        march_epact = 30
    return march_epact

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

for i in range(len(epact)):
    if epact[i] == smart_epact[i]:
        print("OK")
    else:
        print("Not Ok")
"""


for e in range(len(smart_epact)):
    y = year[e]
    print("Year: ", y)

    h = smart_epact[e]
    print("Epact (Jan 1st): ", h)

    #m_e = marchEpact(h, year)
    m_e = h
    print("Epact (March 1st): ", m_e)

    calc1 = 45-h
    print("Paschal Full Moon: ", calc1)

    f = feria[e]
    print("Jan 1st feria: {}".format(f))
    feb = 28
    if y%4==0:
        feb = 29

    #f = ((f+31+feb+calc1)%7)

    dif = h - 14
    f = ((f+31+feb)%7)
    print("difference between {} & 14: {}".format(h,abs(dif)))
    print("1st March Feria: {}".format(f))
    if dif>0:
        lunar14_date = (h + (30-h) + 14)%30
        f += ((30-h) + 14)%7
        print(f)

    if dif<0:
        lunar14_date = h - dif
        f = ((f+(h-dif))%7)
    print("L14: {}".format(lunar14_date))

    # This 24 value was gotten by taking the 1st March Epact, and adding mod 30 to get 14

    if f==0:
        f = 7

    #print("Feria on {} (March 1st): {} ".format(h,f))
    print("Feria on 14: {}".format(f))

    fer_dif = 8-f

    mon="March"
    easter = calc1 + fer_dif
    if easter > 31:
        mon = "April"
        easter = easter%31

    print("Easter: {} {}".format(mon, easter))

    if calc1 <= 25:
        alt = 74-h
        if alt > 31:
            alt = alt%31
        print("if: ", alt)

    else:
        if calc1 > 31:
            calc1 = calc1%31
        print("calc1: ", calc1)

    print()

"""
print(feria)
print(year)
print(index)
"""
