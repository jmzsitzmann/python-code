def sequence(n):
    """print the 3n+1 sequence"""
    counter = 0
    while n != 1:
        counter = counter + 1
        print(n)
        if n % 2 == 0:
            n = n /2
        if n % 2 != 0:
            n = 3*n + 1
    return counter
sequence(144)

for start in range(1, 51):
    sequence(start)