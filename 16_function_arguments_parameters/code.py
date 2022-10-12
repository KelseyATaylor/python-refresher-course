from unittest import result


def add(x,y): #x and y are called parameters
    # pass #Python expects an argument for a function. Pass just means "Do nothing"
    result = x + y
    print(result)

add(5, 3) #These would be called arguments

# -- If a function doesn't have parameter, you can't give it arguments --


def say_hello():
    print("Hello!")


say_hello("Bob")  # Error

# -- But if you add a parameter, then you must give it an argument --


def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Bob")
say_hello()  # Error, needs an argument

# -- Keyword arguments --
# To make things clearer, in Python you can give keyword arguments.


def say_hello(name):
    print(f"Hello, {name}!")


say_hello(name="Bob")  # Obvious that this is someone's name


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(dividend=15, divisor=3)
divide(15, 0)
divide(15, divisor=0)  # That's OK
# divide(dividend=15, 0)  # Not OK, named arguments must go after positional arguments

# I recommend you use keyword arguments whenever possible, just because it makes things much more readable and maintainable long-term.