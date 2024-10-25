salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

current_month = 0
money_capital = 0

while current_month < months:

    if current_month == 0:

        current_spend = spend - salary
        current_month += 1
        money_capital += current_spend

    else:

        current_spend = (spend + (spend * increase)) - salary
        spend += spend * increase
        money_capital += current_spend
        current_month += 1


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
