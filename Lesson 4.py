def kvadrat(x):
    res = x * x
    return res


# print(kvadrat(5))
# print(5*5)

def hello():
    print("Hello World!")

# hello()


def avg(_list):
    return sum(_list) / len(_list)

# print(avg([2,3,4,6,5]))


def pow(x, n=2):
    return x ** n

# print(pow(22, 5))


def max(a, b):
    if a > b:
        return a
    return b


from turtle import Turtle
from random import random


def star(side, n = 5):
    pass


t = Turtle()

t.forward(100)
t.circle(100)

t.screen.mainloop()