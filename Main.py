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