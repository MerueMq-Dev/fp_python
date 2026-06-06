from pymonad.maybe import Just, Nothing,Maybe
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return x + y

add10 = add(10)

just_result = Maybe.apply(add10).to_arguments(Just(5))
print(just_result)

