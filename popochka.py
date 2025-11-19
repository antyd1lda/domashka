#1
import random
import math
a = [random.randint(-20,20) for ss in range(10)]
b = [x for x in a if x < 0 == 0]
c = sum(b)
d = [f for f in a if f % 2 == 0]
f = sum(d)
j = [h for h in a if h % 2  != 0]
e = sum(j)

ss = 1

for i in range(len(a)):
    if i % 3 == 0:
        ss *= a[i]


maximum1 = a.index(max(a))
minimum1 = a.index(min(a))

start = min(minimum1,maximum1)
finish = max(maximum1,minimum1)
iq_rona = 1

for iq in range(start,finish):
    iq_rona *= a[iq]


n = [ad for ad , x in enumerate(a) if x > 0]
start = n[0]
end = n[-1]
r = sum(range(start,end))

print(f"{c}\n{f}\n{e}\n{ss}\n{iq_rona}\n{r}")
#2
aa = [ss for ss in a if ss % 2 == 0]
bb = [sa for sa in a if sa % 2 != 0]
cc = [ca for ca in a if ca < 0 == 0]
dd = [da for da in a if da > 0 == 0]
print(f"{aa}\n{bb}\n{cc}\n{dd}")

