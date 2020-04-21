def print_triangular_numbers(n):
    tri = 0
    for x in n:
        print(x, "\t", tri)
        tri = tri + x
print_triangular_numbers(5)
        