def missing_number(arr, n):
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual

print(missing_number([1, 2, 3, 4, 6], 6) )