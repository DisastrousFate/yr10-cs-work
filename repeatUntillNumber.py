s = 0
n = 1

def checks():
    global s, n

    if s > 29:
        print(s)
    else:
        n = n * 2
        s += n
        checks()
checks()
