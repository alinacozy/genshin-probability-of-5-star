from counting_of_chance import get_chances, chance_of_getting_percents

print("Эта программа выводит, какой у вас шанс выбить легу при известном количестве круток.")
already_pulled = int(input("Введите сколько у вас откручено: "))
my_wishes = int(input("Введите сколько у вас круток: "))
guarantee = input("Есть ли у вас гарант? Y/N: ").upper() == "Y"
chances = get_chances()
print("Ваш шанс выбить желанную легу:", chance_of_getting_percents(already_pulled, my_wishes, guarantee, chances), '%')
