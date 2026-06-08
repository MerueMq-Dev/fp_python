from functools import reduce
from operator import sub, mul, add

def odometer(oksana):
    speeds = oksana[0::2]
    marks  = [0] + oksana[1::2]
    durations = map(sub, marks[1:], marks[:-1])
    distances = map(mul, speeds, durations)
    return reduce(add, distances)

def test():
    cases = [
        # (вход, ожидаемое расстояние, комментарий)
        ([10, 1, 20, 2], 30,  "пример из условия"),
        ([15,1,25,2,30,3,10,5], 90,  "пример из статьи"),
        ([50, 2], 100, "один участок: 50 км/ч * 2 ч"),
        ([10, 1, 0, 5], 10,  "стоянка: вторая скорость 0"),
        ([100, 3, 100, 3], 300, "одинаковые отметки времени — второй участок 0 ч"),
        ([60, 1, 60, 2, 60, 3], 180, "постоянная скорость 60 три часа"),
    ]

    for oksana, expected, note in cases:
        got = odometer(oksana)
        ok = "OK " if got == expected else "FAIL"
        print(f"[{ok}] {note}: ожидали {expected}, получили {got}")

test()