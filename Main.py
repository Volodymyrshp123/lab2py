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