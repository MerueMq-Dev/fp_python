from pymonad.tools import curry
from pymonad.state import State

# Написал калькулятор, который вычисляет арифметические выражения в обратной
# польской записи. Например, 3 5 + 2 * означает (3 + 5) × 2

# кладём число на стек; результатом считаем само положенное число
def push(n):
    def computation(stack):
        new_stack = stack + [n]
        return n, new_stack
    return State(computation)

# снимаем два верхних элемента, применяем операцию, кладём результат обратно
@curry(1)
def binop(fn):
    def computation(stack):
        b = stack[-1]
        a = stack[-2]
        rest = stack[:-2]
        value = fn(a, b)
        return value, rest + [value]
    return State(computation)


add = lambda: binop(lambda a, b: a + b)
sub = lambda: binop(lambda a, b: a - b)
mul = lambda: binop(lambda a, b: a * b)


program = (
    State.insert(None)
    .then(lambda _: push(3))
    .then(lambda _: push(5))
    .then(lambda _: add())
    .then(lambda _: push(2))
    .then(lambda _: mul())
)

result, final_stack = program.run([])
print(result)
print(final_stack)