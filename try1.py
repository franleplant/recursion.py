def fib(n):
    results = [0, 1]
    for i in range(1, n):
        new_value = results[i] + results[i-1]
        results.append(new_value)
    return results[n]


assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
