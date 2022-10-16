money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
while money_capital >= spend:
    month += 1
    money_capital = salary + money_capital
    spend *= 1.05
    money_capital = money_capital - spend
# TODO Оформить решение

print(month)
