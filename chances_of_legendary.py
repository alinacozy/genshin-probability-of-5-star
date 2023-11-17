from counting_of_chance import get_chances, chance_of_getting_percents

print("Эта программа выводит, какой у вас будет шанс выбить легу, если вы накопите какое-либо количество круток.")
already_pulled = int(input("Введите сколько у вас откручено: "))
guarantee = input("Есть ли у вас гарант? Y/N: ").upper() == "Y"
chances = get_chances()

count_to_guaranteed_legendary = 90 - already_pulled if guarantee else 180 - guarantee  # столько круток до гаранта
for i in range(1, count_to_guaranteed_legendary + 1):
    print("Круток: ", i, ", Шанс выбить легу: ", chance_of_getting_percents(already_pulled, i, guarantee, chances), "%")
