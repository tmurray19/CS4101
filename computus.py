def IanTaylorEasterJscr(year):
 a = year % 19
 b = year >> 2
 c = b // 25 + 1
 d = (c * 3) >> 2
 e = ((a * 19) - ((c * 8 + 5) // 25) + d + 15) % 30
 e += (29578 - a - e * 32) >> 10
 e -= ((year % 7) + b - d + e + 2) % 7
 d = e >> 5
 day = e - d * 31
 month = d + 3
 return year, month, day


print(IanTaylorEasterJscr(2019))
input()
