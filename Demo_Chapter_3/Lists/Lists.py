    squares = [1, 4, 9, 16, 25]
    print(squares)

print(squares[0])

print(squares[-1])

print(squares[:])

squares.append(345)
squares.append(7**3)
print(squares)
print(len(squares))

squares.remove(1)
index=squares.count(16)
print(index)