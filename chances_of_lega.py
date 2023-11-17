from counting_of_chance import get_chances, chance_of_getting_percents

print("Эта программа выводит, какой у вас будет шанс выбить легу, если вы накопите какое-либо количество круток.")
otkrucheno = int(input("Введите сколько у вас откручено: "))
garant = input("Есть ли у вас гарант? Y/N: ").upper() == "Y"
chances = get_chances()

count_to_garant = 90 - otkrucheno if garant else 180 - garant  # столько круток до гаранта
for i in range(1, count_to_garant + 1):
    print("Круток: ", i, ", Шанс выбить легу: ", chance_of_getting_percents(otkrucheno, i, garant, chances), "%")
