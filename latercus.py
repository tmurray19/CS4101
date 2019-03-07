"""
Some pythonic testing of latercus

"""

# Dabhi paper version of latercus
year = []
index = []
feria = [7]
epact = [
        20,1,12,23,4,15,26,7,18,29,10,21,2,13,25,6,17,28,9,
        20,1,12,23,4,15,26,7,18,30,11,22,3,14,25,6,17,28,9,
        20,1,12,23,5,16,27,8,19,30,11,22,3,14,25,6,17,28,10,
        21,2,13,24,5,16,27,8,19,30,11,22,3,15,26,7,18,29,10,
        21,2,13,24,5,16,27,8
        ]

oxford-epact = [
    

    ]

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




print(feria)
print(year)
print(index)
