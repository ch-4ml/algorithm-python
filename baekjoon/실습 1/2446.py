n = int(input())
for i in range(2 * n - 1):
    print(" " * i + "*" * (2 * n - 2 * i - 1) if i < n else " " * (2 * n - i - 2)  + "*" * (2 * i - 2 * n + 3))