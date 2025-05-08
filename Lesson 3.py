def printLine(count, symbol = "*"):
    print(symbol * count)

printLine(20)
#
# print("mama")
#
printLine(30, '$')
#
# print("Hello")
#
# printLine(40, '#')
# printLine(10, 'mama ')

def summa(a, b):
    c = a + b
    return c

# res = summa(23, 3)
# print(summa(3, 5))


def square(n):
    printLine("* ", n)
    for i in range(n-2):
        print("* ", end='')
        for j in range(n-2):
            print("  ", end='')
        print("* ", end='')
        print()
    printLine("* ", n)



# square(4)

# * * * * *
# *       *
# *       *
# *       *
# * * * * *