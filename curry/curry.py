from pymonad.tools import curry

@curry(2)
def greet(greetings, name):
    return f"{greetings}, {name}"

@curry(4)
def formatGreeting(greetings, punctuation, end_punctuation, name):
    return f"{greetings}{punctuation} {name}{end_punctuation}"


sayHello = greet("Hello");