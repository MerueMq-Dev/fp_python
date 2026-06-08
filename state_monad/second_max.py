from functools import reduce
def second_max(numbers):
    def update(top_two, x):
        first, second = top_two
        if x >= first:
            return (x, first)
        elif x > second:
            return (first, x)
        else:
            return (first, second)

    first, second = reduce(update, numbers, (float('-inf'), float('-inf')))
    return second

print(second_max([5, 4, 3, 2, 5]))   # 5
print(second_max([1, 2, 3, 4, 5]))   # 4
print(second_max([7]))