# Bai 1
print("Bai 1:")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập một số nguyên dương n: "))
if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")

# Bai 2
print("Bai 2:")
def factorial(n):
    if n == 0:
        return 1
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

n = int(input("Nhập một số nguyên không âm n: "))
if n < 0:
    print("Vui lòng nhập một số nguyên không âm!")
else:
    print(f"{n}! = {factorial(n)}")

# Bai 3
print("Bai 3:")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input("Nhập số phần tử của mảng: "))
arr = []
print("Nhập các phần tử của mảng:")
for i in range(n):
    arr.append(int(input()))

bubble_sort(arr)
print("Mảng sau khi sắp xếp theo thứ tự tăng dần:")
print(arr)

# Bai 4
print("Bai 4:")
def fibonacci(n):
    fib = [0] * (n + 1)
    if n >= 1:
        fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

n = int(input("Nhập n: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
