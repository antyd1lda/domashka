#чуть чуть халатно написал сорян
import random
print(eval(input("введите значение: ")))
a = [random.randint(-10,20) for ss in range(10)]

mini = min(a)
maxi = max(a)

men = []
bol = []
zero = []

for si in a:
    if si < 0:
        men.append(si)
    elif si > 0:
        bol.append(si)
    elif si == 0:
        zero.append(si)

print(f"""
минимальное число: {mini}
максимальное число: {maxi}
количество отрицательных чисел: {len(men)}
количество максимальных чисел: {len(bol)}
количество нулей: {len(zero)}
""")

