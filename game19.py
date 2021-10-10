def move():
    global mass
    global m
    global n
    n1 = mass[n[0]][n[1]]
    m1 = mass[m[0]][m[1]]
    if n1 == "#" or m1 == "#":
        print("illegal move")
    else:
        n1 = int(n1)
        m1 = int(m1)
        if n1 + m1 == 10 or n1 == m1:
            mass[n[0]][n[1]] = "#"
            mass[m[0]][m[1]] = "#"
            display()
        else:
            print("illegal move")


def display():
    global mass
    print("   abcdefghi")
    l = len(mass)
    last = len(mass[l - 1])
    for i in range(l):
        if i <= 9:
            table = f"{i}  "
        else:
            table = f"{i} "
        print(f"{table}", end="")
        ex = 9
        if i == l - 1:
            ex = last
        for j in range(ex):
            print(mass[i][j], end="")
        print()


def check():
    global mass
    k = True
    l = len(mass)
    last = len(mass[l - 1])
    for i in range(l):
        ex = 9
        if i == l - 1:
            ex = last
        for j in range(ex):
            if mass[i][j] != "#":
                k = False
                break
    return k


def check_for_moves():
    global mass
    k = False
    l = len(mass)
    last = len(mass[l - 1])
    for i in range(l):
        x1 = 0
        x2 = 0
        s = len(mass[i])
        c = 0
        temp = 0
        for j in range(s):
            if mass[i][j] != "#" and c == 0:
                x1 = mass[i][j]
                c += 1
            elif mass[i][j] != "#" and c == 1:
                x2 = mass[i][j]
                c += 1
                temp = j
                break
        if c == 2:
            if x1 != "#" and x2 != "#":
                if x1 == x2 or int(x1) + int(x2) == 10:
                    k = True
            while temp != s:
                if x1 != "#" and x2 != "#":
                    if x1 == x2 or int(x1) + int(x2) == 10:
                        k = True
                        break
                temp += 1
                if temp != s:
                    if mass[i][temp] != "#":
                        x1, x2 = x2, mass[i][temp]
    if not k:
        for i in range(9):
            x1 = 0
            x2 = 0
            c = 0
            temp = 0
            height = l
            if i >= last:
                height -= 1
            for j in range(height):
                if mass[j][i] != "#" and c == 0:
                    x1 = mass[j][i]
                    c += 1
                elif mass[j][i] != "#" and c == 1:
                    x2 = mass[j][i]
                    c += 1
                    temp = j
                    break
            if c == 2:
                if x1 != "#" and x2 != "#":
                    if x1 == x2 or int(x1) + int(x2) == 10:
                        k = True
                while temp != height:
                    if x1 != "#" and x2 != "#":
                        if x1 == x2 or int(x1) + int(x2) == 10:
                            k = True
                            break
                    temp += 1
                    if temp != height:
                        if mass[temp][i] != "#":
                            x1, x2 = x2, mass[temp][i]
    return k


def mass_reload():
    b = []
    global count
    global mass
    k = True
    l = len(mass)
    last = len(mass[l - 1])
    for i in range(l):
        ex = 9
        if i == l - 1:
            ex = last
        for j in range(ex):
            if mass[i][j] != "#":
                b.append(mass[i][j])
    count += len(b)
    for i in range(len(b)):
        l = len(mass)
        if len(mass[l - 1]) == 9:
            mass.append([b[i]])
        else:
            mass[l - 1].append(b[i])


def dig_number(x):
    h = True
    y = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    letter = x[0]
    if letter not in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
        return 0

    else:
        ind = y.index(letter) + 1
        try:
            digit = int(x[1:])
        except:
            h = False
        if h:
            return digit * 9 + ind
        else:
            return 0



count = 27
mass = [["1", "2", "3", "4", "5", "6", "7", "8", "9"],
     ["1", "1", "1", "2", "1", "3", "1", "4", "1"],
     ["5", "1", "6", "1", "7", "1", "8", "1", "9"]]
display()


while not check():
    if not check_for_moves():
        mass_reload()
        print()
        print("no moves left")
        print()
        display()
    print("waiting for the move")
    a = input()
    b = input()
    a = dig_number(a)
    b = dig_number(b)
    if a < 1 or a > count or b < 1 or b > count or a == b:
        print("illegal move")
    else:
        m = [(a - 1) // 9, (a - 1) % 9]
        n = [(b - 1) // 9, (b - 1) % 9]
        if m[0] == n[0]:
            if abs(m[1] - n[1]) == 1:
                move()
            elif abs(m[1] - n[1]) > 1:
                p = True
                l = min(m[1], n[1])
                u = max((m[1]), n[1])
                for i in range(l + 1, u):
                    if mass[m[0]][i] != "#":
                        p = False
                        break
                if p:
                    move()
                else:
                    print("illegal move")
            else:
                print("illegal move")
        elif m[1] == n[1]:
            if abs(m[0] - n[0]) == 1:
                move()
            elif abs(m[0] - n[0]) > 1:
                p = True
                l = min(m[0], n[0])
                u = max((m[0]), n[0])
                for i in range(l + 1, u):
                    if mass[i][m[1]] != "#":
                        p = False
                        break
                if p:
                    move()
                else:
                    print("illegal move")
            else:
                print("illegal move")
        else:
            print("illegal move")
print("you win")