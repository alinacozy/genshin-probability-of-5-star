from counting_of_chance import get_chances, chance_of_getting_percents

print("Эта программа выводит, сколько круток вам нужно накопить, чтобы выбить легу с желаемым шансом.")
otkrucheno = int(input("Введите сколько у вас откручено: "))
garant = input("Есть ли у вас гарант? Y/N: ").upper() == "Y"
goal_chance = int(input("С какой вероятностью хотите выбить легу? Введите число в процентах: "))
chances = get_chances()

chance = 0
i = 1  # переменная, по которой мы перебираем количество круток
while chance < goal_chance:
    chance = chance_of_getting_percents(otkrucheno, i, garant, chances)
    i += 1

print(f"Вы должны накопить столько круток: {i}")
print(f"Тогда ваша лега выпадет с шансом: {chance}%")
