a = []
b = []
number = input()

while number != "!":
    a.append(int(number))
    number = input()

def find_minimum():
    minimum = a[0]
    for i in range(0, len(a)):
        if a[i] < minimum:
            minimum = a[i]
    return minimum


def rra():
    global a
    a = a[-1:] + a[:-1]
    print("rra")


def pb():
    global a
    global b
    if len(a)!=0:
        b.append(a[0])
        b = b[-1:] + b[:-1]
        a.pop(0)
        print("pb")


def pa():
    global a
    global b
    if len(b) != 0:
        a.append(b[0])
        a = a[-1:] + a[:-1]
        b.pop(0)
        print("pa")

while len(a) != 0:
    minimum1 = find_minimum()
    while a[0] != minimum1:
        rra()
    pb()

while len(b) != 0:
    pa()
