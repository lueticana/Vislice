def prastevila(n):
    for i in range(1, n + 1):
        if prastevilo(i):
            print(i)

def prastevilo(n):
    for i in range (2, round(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False
        return True

prastevila(200)