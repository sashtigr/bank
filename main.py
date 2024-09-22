import sqlite3


db = sqlite3.connect('bank.db')

#Create Cursor
c = db.cursor()

# c.execute("""CREATE TABLE credits (
#     type text,
#     name text,
#     percentage integer
# )""")
#
#
# c.execute("INSERT INTO credits VALUES ('Contribution', 'Best Percent', 20)")
# c.execute("INSERT INTO credits VALUES ('Contribution', 'SmartContribution',15)")
# c.execute("INSERT INTO credits VALUES ('Contribution', 'AlfaContribute',19)")
# c.execute("INSERT INTO credits VALUES ('Credit', 'AutoCredit', 28)")
# c.execute("INSERT INTO credits VALUES ('Credit', 'Ipoteka',22)")
# c.execute("INSERT INTO credits VALUES ('Credit', 'GoalCredit',34)")


while True:

    print("Выберите тип операции:" "\n"
          "1: Оформить вклад \n"
          "2: Оформить кредит \n"
          "3: Завершить работу программы"
    )

    choise = int(input())

    if choise == 1:
        c.execute("SELECT rowid, * FROM credits WHERE type = 'Contribution'")
        items = c.fetchall()
        for el in items:
            print(el)
        selection = int(input("Выберите интересующий вас вклад:\n"))

        if selection == 1:
            sum = int(input("Введите сумму, которую хотите вложить:"))
            year = int(input("Введите количество лет, на которые хотите открыть влкад:"))
            print("Вы выбрали влкад 'Лучший процент' на сумму ", sum, " на ", year, "года")
            print("Через", year, "года ваша сумма будет равна", sum+sum*0.2*year)
            print("Из них чистая прибыль: ", sum*0.2*year)
            for i in range (year):
                sum += sum*0.2
            print("Если после каждого года, полученные проценты будут добавляться в тело вклада, то итоговая сумма составит", sum)

        if selection == 2:
            sum = int(input("Введите сумму, которую хотите вложить:"))
            year = int(input("Введите количество лет, на которые хотите открыть влкад:"))
            print("Вы выбрали влкад 'Умный вклад' на сумму ", sum, " на ", year, "года")
            print("Через", year, "года ваша сумма будет равна", sum+sum*0.19*year)
            print("Из них чистая прибыль: ", sum*0.19*year)
            for i in range (year):
                sum += sum*0.19
            print("Если после каждого года, полученные проценты будут добавляться в тело вклада, то итоговая сумма составит", sum)

        if selection == 3:
            sum = int(input("Введите сумму, которую хотите вложить:"))
            year = int(input("Введите количество лет, на которые хотите открыть влкад:"))
            print("Вы выбрали влкад 'Лучший процент' на сумму ", sum, " на ", year, "года")
            print("Через", year, "года ваша сумма будет равна", sum+sum*0.15*year)
            print("Из них чистая прибыль: ", sum*0.15*year)
            for i in range (year):
                sum += sum*0.15
            print("Если после каждого года, полученные проценты будут добавляться в тело вклада, то итоговая сумма составит", sum)


    elif choise == 2:
        c.execute("SELECT rowid, * FROM credits WHERE type = 'Credit'")
        items = c.fetchall()
        for el in items:
            print(el)
        selection = int(input("Выберите кредит\n"))
        if selection == 4:
            sum = int(input("Введите сумму, которую хотите получить:"))
            print("Выберите способ выплаты кредита")
            print("1) Фиксированное количество месяцев")
            print("2) Фиксированная сумма")
            way = int(input())
            if way == 1:
                creditYear = int(input("Введите количество месяцев"))
                platezh = (sum + sum*0.28)/creditYear
                print("Ваш ежемесячный платеж = ",platezh)
            if way == 2:
                creditPlatezh = int(input("Введите желаемый ежемесячный платеж"))
                remainTime = 0
                while sum > 0:
                    sum = (sum + (sum*0.28)/12) - creditPlatezh
                    remainTime+=1
                print("Вы будете выплачивать кредит ", remainTime, " месяцев")
        if selection == 5:
            sum = int(input("Введите сумму, которую хотите получить:"))
            print("Выберите способ выплаты кредита")
            print("1) Фиксированное количество месяцев")
            print("2) Фиксированная сумма")
            way = int(input())
            if way == 1:
                creditYear = int(input("Введите количество месяцев"))
                platezh = (sum + sum*0.22)/creditYear
                print("Ваш ежемесячный платеж = ",platezh)
            if way == 2:
                creditPlatezh = int(input("Введите желаемый ежемесячный платеж"))
                remainTime = 0
                while sum > 0:
                    sum = (sum + (sum*0.22)/12) - creditPlatezh
                    remainTime+=1
                print("Вы будете выплачивать кредит ", remainTime, " месяцев")
        if selection == 6:
            sum = int(input("Введите сумму, которую хотите получить:"))
            print("Выберите способ выплаты кредита")
            print("1) Фиксированное количество месяцев")
            print("2) Фиксированная сумма")
            way = int(input())
            if way == 1:
                creditYear = int(input("Введите количество месяцев"))
                platezh = (sum + sum*0.34)/creditYear
                print("Ваш ежемесячный платеж = ",platezh)
            if way == 2:
                creditPlatezh = int(input("Введите желаемый ежемесячный платеж"))
                remainTime = 0
                while sum > 0:
                    sum = (sum + (sum*0.34)/12) - creditPlatezh
                    remainTime+=1
                print("Вы будете выплачивать кредит ", remainTime, " месяцев")
    elif choise == 3:
        break

db.commit()

db.close()