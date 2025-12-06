def show_quote():
    print("“Don't let the noise of others' opinions\ndrown out your own inner voice.”\n\t\tSteve Jobs")

def show_odd_numbers(a, b):
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()

def draw_line(length, direction, symbol):
    if direction == 'h':
        print(symbol * length)
    elif direction == 'v':
        print((symbol + '\n') * length)

def max_of_four(a, b, c, d):
    return max(a, b, c, d)

def sum_in_range(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

def is_prime(num):
    if num < 2: return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_lucky(num):
    s = str(num)
    if len(s) != 6: return False

    return sum(map(int, s[:3])) == sum(map(int, s[3:]))

print("1:")
show_quote()

print("\n 2: (нечетные между 10 и 20):")
show_odd_numbers(10, 20)

print("\n 3: (линия):")
draw_line(5, 'h', '*')

print("\n 4: (максимум из 5, 12, 3, 8):")
print(max_of_four(5, 12, 3, 8))

print("\n 5: (сумма от 1 до 5):")
print(sum_in_range(1, 5))

print("\n 6: (простое ли 13? А 12?):")
print(is_prime(13))
print(is_prime(12))

print("\n 7: (Счастливое 123420?):")
print(is_lucky(123420))