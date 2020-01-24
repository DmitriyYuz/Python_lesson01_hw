
revenue = float(input('Какова выручка вашей фирмы? '))
costs = float(input('Каковы издержки вашей фирмы? '))

if revenue > costs:
    print('Работаем с прибылью')
    profitability = revenue - costs
    staff = int(input('Численность сотрудников вашей фирмы? '))
    print('Прибыль на сотрудника: ', profitability / staff)
elif revenue <= costs:
    print('Раблотаем с убытком')

