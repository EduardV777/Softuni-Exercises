def squares(n):
    val = 1
    for k in range(1, n + 1):
        val = k ** 2
        yield val


print(list(squares(5)))