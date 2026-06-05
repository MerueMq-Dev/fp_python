from curry.curry import sayHello, formatGreeting


if __name__ == '__main__':
    result = sayHello("Ivan")
    print(result)

    final = formatGreeting("Hello")(",")("!")
    final_result = final("Petya")
    print(final_result)