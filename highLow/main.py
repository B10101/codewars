def high_and_low(numbers):
    li = numbers.split()
    fin = list(map(int, li))
    return f"{max(fin)} {min(fin)}"


print(high_and_low('1 2 -3 4 5'))
    