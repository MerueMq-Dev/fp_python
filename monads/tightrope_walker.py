from pymonad.maybe import Just, Nothing
from pymonad.tools import curry


@curry(2)
def to_left(num, pole):
    l, r = pole
    if abs((l + num) - r) > 4:
        return Nothing
    return Just((l + num, r))


@curry(2)
def to_right(num, pole):
    l, r = pole
    if abs((r + num) - l) > 4:
        return Nothing
    return Just((l, r + num))

def banana(pole):
    return Nothing

def show(maybe):
    if maybe is Nothing:
        print("Упал!")
    else:
        l, r = maybe.value
        print("Держится:", l, r)


# начальное состояние: 0 птиц слева, 0 справа
begin = Just((0, 0))

# канатоходец упадёт на последнем шаге
show(
    begin.bind(to_left(2)).bind(to_right(5)).bind(to_left(-2))
)

# здесь всё в порядке
show(
    begin.bind(to_left(2)).bind(to_right(5)).bind(to_left(-1))
)

# кожура всё испортит
show(
    begin.bind(to_left(2)).bind(banana).bind(to_right(5)).bind(to_left(-1))
)