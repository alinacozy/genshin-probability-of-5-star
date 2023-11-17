import requests


def chance_of_getting(otkrucheno: int, my_krutki: int, garant: bool, chances: list[int]):
    if my_krutki + otkrucheno >= 180 or (garant and my_krutki + otkrucheno >= 90):
        return 1
    if my_krutki == 0:
        return 0
    if my_krutki == 1:  # условие выхода из рекурсии
        return chances[otkrucheno] if garant else chances[otkrucheno] / 2
    if not garant:  # если нет гаранта
        chance_of_any_lega = ((chances[otkrucheno] / 2) +  # шанс выбить желанную легу
                              (chances[otkrucheno] / 2) * chance_of_getting(0, my_krutki - 1, True,
                                                                            chances))  # шанс выбить чичу и тд
        if 1 - chances[otkrucheno]:
            return (chance_of_any_lega +
                    (1 - chances[otkrucheno]) * chance_of_getting(otkrucheno + 1, my_krutki - 1, garant,
                                                                  chances))  # шанс не выбить легу
        # если у нас 89 крутка (предпоследняя перед гарантом)
        return chance_of_any_lega
    # если есть гарант
    return ((chances[otkrucheno]) +  # шанс выбить желанную легу
            ((1 - chances[otkrucheno]) * chance_of_getting(otkrucheno + 1, my_krutki - 1, garant,
                                                           chances)))  # шанс не выбить легу


def chance_of_getting_percents(otkrucheno: int, my_krutki: int, garant: bool, chances: list[int]):
    return round(chance_of_getting(otkrucheno, my_krutki, garant, chances)*100, 2)

def get_chances():
    r = requests.get('https://api.paimon.moe/wish?banner=300056')
    data = r.json()
    pityCount = data["pityCount"]["legendary"]  # сколько на данной крутке выпало лег
    pityCount = pityCount[1:91]  # обрезание массива
    countEachPity = data["countEachPity"]  # сколько всего сделано данных круток
    chances = []  # массив шансов
    for i in range(len(pityCount)):
        if countEachPity[i]:
            chances.append(min(pityCount[i] / countEachPity[i], 1))
        else:
            chances.append(0)
    return chances
