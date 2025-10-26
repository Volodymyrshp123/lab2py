print("Task1")
numbers = 49,52,87,23,64,25,55,34,2,10
for num in numbers:
    if num < 50:
        print("Менше 50:", num)
    else:
        print("Більше або рівне 50:", num)
    
print("Task2")
amount = float(input("Введіть суму покупки (грн): "))

if amount > 1000:
    discount = 0.05
elif amount > 500:
    discount = 0.03
else:
    discount = 0.0

final_price = amount - (amount * discount)

print(f"Знижка: {discount * 100:.0f}%")
print(f"Сума до сплати: {final_price:.2f} грн")
print("Task3")
a = int(input("Введіть довжину основи (a): "))
h = int(input("Введіть висоту (h): "))
S = (a * h) / 2
print(f"Площа трикутника: {S}")
if S //2 == 0:
    sum = S / 2
    print(f"Половина площі: {sum}")
else:
    print("Не можу ділити на 2!")
print("Task4")
A = int(input("Введіть число A: "))
B = int(input("Введіть число B: "))

if A >= B:
    print("Помилка: A повинно бути менше за B.")
else:
    total = 0
    for i in range(A, B + 1):
        total += i
    print(f"Сума всіх цілих чисел від {A} до {B} включно: {total}")
print("Task5")
D = int(input("Введіть число D: "))
E = int(input("Введіть число E: "))
if D >= E:
        print("Помилка: D повинно бути менше за E.")
else:
        total = 0
        for i in range(D, E + 1):
            total += i ** 2
print(f"Сума квадратів всіх цілих чисел від {D} до {E} включно: {total}")
print("Task6")
a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))
if a >= b:
    print("Помилка: b повинно бути більше за a.")
else:
    total = 0
    current = a
    while current <= b:
        total += current
        current += 1
    print(f"Сума всіх цілих чисел від {a} до {b} включно: {total}")
print("Task7")
T = int(input("Введіть число T: "))
if not 0 <= T <= 50:
    print("Помилка: T повинно бути в межах від 0 до 50.")
else:
    p = 50
    total = 0
    for i in range(T, p + 1):
        total += i ** 2
    print(f"Сума квадратів всіх цілих чисел від {T} до {p} включно: {total}")
    print("Task8")
    N = int(input("Введіть ціле число N (>1): "))
K = 0
while 5 ** K <= N:
    K += 1
print(f"Найменше ціле K, при якому 5^{K} > {N}, це: {K}")
print("Task9")
M = int(input("Введіть ціле число M: "))
m =1, 4, 9, 16, 25, 36, 49, 64, 81, 100
for num in m:
    if num > M:
        print(num)
        break
print("Task10")
n = int(input("Введіть число n: "))
a = 1
d = 1

while a <= n:
    d += 2
    a += d

print(f"Перше число з ряду, більше за {n}: {a}")
print("Task11")
D = int(input("Введіть день: "))
M = int(input("Введіть місяць: "))

names = [
    "Козеріг", "Водолій", "Риби", "Овен", "Телець", "Близнюки",
    "Рак", "Лев", "Діва", "Терези", "Скорпіон", "Стрілець", "Козеріг"
]

starts = [
    (22, 12), (20, 1), (19, 2), (21, 3), (20, 4), (21, 5),
    (22, 6), (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (1, 1)
]

ends = [
    (19, 1), (18, 2), (20, 3), (19, 4), (20, 5), (21, 6),
    (22, 7), (22, 8), (22, 9), (22, 10), (22, 11), (21, 12), (19, 1)
]

i = 0
found = 0

while i < len(names) and found == 0:
    start_day = starts[i][0]
    start_month = starts[i][1]
    end_day = ends[i][0]
    end_month = ends[i][1]

    found += (M == start_month and D >= start_day) * 1
    found += (M == end_month and D <= end_day) * 1

    i += (1 - found) 

print("Ваш знак Зодіаку:", names[i - 1])
print("Task12")
unit = int(input("Введіть номер одиниці маси (1–5):\n1. Кілограм\n2. Міліграм\n3. Грам\n4. Тонна\n5. Центнер\n"))
value = float(input("Введіть масу тіла: "))

match unit:
    case 1:  
        mass_in_kg = value
    case 2:  
        mass_in_kg = value * 0.000001
    case 3: 
        mass_in_kg = value * 0.001
    case 4:  
        mass_in_kg = value * 1000
    case 5:  
        mass_in_kg = value * 100
    case _:
        mass_in_kg = None

if mass_in_kg is not None:
    print(f"Маса тіла у кілограмах: {mass_in_kg}")
else:
    print("Невірний номер одиниці маси.")