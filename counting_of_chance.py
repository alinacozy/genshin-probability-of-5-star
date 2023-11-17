import requests


def chance_of_getting(already_pulled: int, my_wishes: int, guarantee: bool, chances: list[int]) -> float:
    if my_wishes + already_pulled >= 180 or (guarantee and my_wishes + already_pulled >= 90):
        return 1.0
    if my_wishes == 0:
        return 0.0
    if my_wishes == 1:  # условие выхода из рекурсии
        return chances[already_pulled] if guarantee else chances[already_pulled] / 2
    if not guarantee:  # если нет гаранта
        chance_of_any_lega = ((chances[already_pulled] / 2) +  # шанс выбить желанную легу
                              (chances[already_pulled] / 2) * chance_of_getting(0, my_wishes - 1, True,
                                                                                chances))  # шанс выбить чичу и тд
        if 1 - chances[already_pulled]:
            return (chance_of_any_lega +
                    (1 - chances[already_pulled]) * chance_of_getting(already_pulled + 1, my_wishes - 1, guarantee,
                                                                      chances))  # шанс не выбить легу
        # если у нас 89 крутка (предпоследняя перед гарантом)
        return chance_of_any_lega
    # если есть гарант
    return ((chances[already_pulled]) +  # шанс выбить желанную легу
            ((1 - chances[already_pulled]) * chance_of_getting(already_pulled + 1, my_wishes - 1, guarantee,
                                                               chances)))  # шанс не выбить легу


def chance_of_getting_percents(already_pulled: int, my_wishes: int, guarantee: bool, chances: list[int]):
    return round(chance_of_getting(already_pulled, my_wishes, guarantee, chances) * 100, 2)


def get_chances():
    r = requests.get('https://api.paimon.moe/wish?banner=300056')
    data = r.json()
    pity_count = data["pityCount"]["legendary"]  # сколько на данной крутке выпало лег
    pity_count = pity_count[1:91]  # обрезание массива
    count_each_pity = data["countEachPity"]  # сколько всего сделано данных круток
    chances = []  # массив шансов
    for i in range(len(pity_count)):
        if count_each_pity[i]:
            chances.append(min(pity_count[i] / count_each_pity[i], 1))
        else:
            chances.append(0)
    return chances
