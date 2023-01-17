price_1 = 0
price_2 = 990
price_3 = 1390
ticket_sum = 0
ticket_count = 0

N = int(input("Введите количество билетов: "))

ticket_count = N

for N in range(1, N + 1):
    visitor_age = int(input("Введите возраст посетителя: "))
    if visitor_age < 18:
        print("Стоимость билета составит: ", price_1, "руб.")
        ticket_count += 1
        ticket_sum = ticket_sum + price_1
    elif visitor_age == 18 or visitor_age < 25:
        print("Стоимость билета составит: ", price_2, "руб.")
        ticket_count += 1
        ticket_sum = ticket_sum + price_2
    else:
        print("Стоимость составит: ", price_3, "руб.")
        ticket_count += 1
        ticket_sum = ticket_sum + price_3
if N > 3:
    ticket_sum = ticket_sum * 0.9

while ticket_count <= N:
    break

print("***********")
print("Сумма к оплате: ", ticket_sum, "руб.")