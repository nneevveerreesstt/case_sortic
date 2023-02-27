a = []
b = []
number = input()

while number != "!":
    a.append(int(number))
    number = input()

commands = []
command = input()
while command != "*":
    commands.append(command)
    command = input()

def find_minimum():
    minimum = a[0]
    for i in range(0, len(a)):
        if a[i] < minimum:
            minimum = a[i]
    return minimum

def sa():
    global a
    if len(a)>1:
        a1 = a[0]
        a2 = a[1]
        a[0] = a2
        a[1] = a1

def sb():
    global b
    if len(b) > 1:
        b1 = b[0]
        b2 = b[1]
        b[0] = b2
        b[1] = b1

def ss():
    global a
    global b
    if len(a) > 1:
        a1 = a[0]
        a2 = a[1]
        a[0] = a2
        a[1] = a1
    if len(b) > 1:
        b1 = b[0]
        b2 = b[1]
        b[0] = b2
        b[1] = b1

def pa():
    global a
    global b
    if len(b) != 0:
        a.append(b[0])
        a = a[-1:] + a[:-1]
        b.pop(0)

def pb():
    global a
    global b
    if len(a)!=0:
        b.append(a[0])
        b = b[-1:] + b[:-1]
        a.pop(0)

def ra():
    global a
    a = a[1:] + a[:1]

def rb():
    global b
    b = b[1:] + b[:1]

def rr():
    global a
    global b
    a = a[1:] + a[:1]
    b = b[1:] + b[:1]

def rra():
    global a
    a = a[-1:] + a[:-1]

def rrb():
    global b
    b = b[-1:] + b[:-1]

def rrr():
    global a
    global b
    a = a[-1:] + a[:-1]
    b = b[-1:] + b[:-1]

flag = True

for i in range(len(commands)):
    if commands[i] == "sa":
        sa()
    elif commands[i] == "sb":
        sb()
    elif commands[i] == "ss":
        ss()
    elif commands[i] == "pa":
        pa()
    elif commands[i] == "pb":
        pb()
    elif commands[i] == "ra":
        ra()
    elif commands[i] == "rb":
        rb()
    elif commands[i] == "rr":
        rr()
    elif commands[i] == "rra":
        rra()
    elif commands[i] == "rrb":
        rrb()
    elif commands[i] == "rrr":
        rrr()
    else:
        print("KO")
        flag = False
        break

flag1 = True

if flag == True:
    for i in range(1, len(a)):
        if a[i-1]>a[i]:
            flag1 = False
            break
    if flag1 == False:
        print("KO")
    else:
        print("OK")
