from counting_of_chance import get_chances, chance_of_getting_percents
import matplotlib.pyplot as plt
import numpy as np

print("Эта программа выводит график зависимости вероятности получить легу от количества круток.")
already_pulled = int(input("Введите сколько у вас откручено: "))
guarantee = input("Есть ли у вас гарант? Y/N: ").upper() == "Y"
chances = get_chances()

count_to_guaranteed_legendary = 90 - already_pulled if guarantee else 180 - already_pulled  # столько круток до гаранта
probabilities = []
for i in range(count_to_guaranteed_legendary + 1):
    probabilities.append(chance_of_getting_percents(already_pulled, i, guarantee, chances))

fig, ax = plt.subplots()
ax.set_title(f"Зависимость шанса выпадения леги от числа круток.\n " +
             f"Откручено: {already_pulled}, гарант: {'есть' if guarantee else 'нет'}.")  # заголовок
ax.set_xlabel("Число круток")  # ось абсцисс
ax.set_ylabel("Шанс выпадения леги в процентах")  # ось ординат
x = np.linspace(0, count_to_guaranteed_legendary, count_to_guaranteed_legendary + 1)
ax.plot(x, probabilities)
plt.grid()
step = count_to_guaranteed_legendary // 19 + 1  # оптимальный целый шаг по x (подобран на глазок)
x_ticks = np.linspace(0, (count_to_guaranteed_legendary // step) * step, count_to_guaranteed_legendary // step + 1)
y_ticks = np.linspace(0, 100, 11)
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
plt.xlim(0, count_to_guaranteed_legendary)
plt.ylim(0, 100 + 5)
plt.show()
