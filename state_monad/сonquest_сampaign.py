from functools import reduce

def conquest_campaign(width, height, landing_count, battalion):
    # массив должен содержать ровно landing_count пар координат
    assert len(battalion) == 2 * landing_count, (
        f"ожидалось {2 * landing_count} координат "
        f"({landing_count} точек высадки), получено {len(battalion)}"
    )

    # разбиваем плоский массив [x1,y1, x2,y2, ...] на пары координат
    landing_points = set(zip(battalion[::2], battalion[1::2]))

    def simulate_day(captured, day_number):
        expanded = captured | {
            (x + dx, y + dy)
            for (x, y) in captured
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if 1 <= x + dx <= width and 1 <= y + dy <= height
        }
        if expanded == captured:  # волна перестала расти — всё захвачено
            return day_number
        return simulate_day(expanded, day_number + 1)

    return simulate_day(landing_points, 1)

def test():
    cases = [
        # (width, height, landing_count, battalion, ожидаемый_день, комментарий)
        (3, 4, 2, [2,2, 3,4], 3, "пример из условия"),
        (1, 1, 1, [1,1], 1, "одна клетка — захвачена сразу"),
        (1, 5, 1, [1,1], 5, "полоска 1x5, старт с края"),
        (1, 5, 1, [1,3], 3, "полоска 1x5, старт в центре"),
        (5, 5, 1, [1,1], 9, "угол поля 5x5: (5-1)+(5-1)+1"),
        (5, 5, 1, [3,3], 5, "центр поля 5x5"),
        (3, 3, 4, [1,1, 1,3, 3,1, 3,3], 3, "четыре угла")
    ]

    for width, height, landing_count, battalion, expected, note in cases:
        got = conquest_campaign(width, height, landing_count, battalion)
        if expected is None:
            print(f"info {note}: получили {got}")
        else:
            ok = "OK " if got == expected else "FAIL"
            print(f"{ok} {note}: ожидаем {expected}, получили {got}")

test()