from counting_of_chance import get_chances, chance_of_getting_percents

print("Эта программа выводит, какой у вас шанс выбить легу при известном количестве круток.")
otkrucheno = int(input("Введите сколько у вас откручено: "))
my_krutki = int(input("Введите сколько у вас круток: "))
garant = input("Есть ли у вас гарант? Y/N: ").upper() == "Y"
chances = get_chances()
print("Ваш шанс выбить желанную легу:", chance_of_getting_percents(otkrucheno, my_krutki, garant, chances), '%')
