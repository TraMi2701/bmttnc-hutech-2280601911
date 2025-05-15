
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Nhập số: "))
if is_prime(num):
    print(f"{num} là số nguyên tố.")
else:
    print(f"{num} không là số nguyên tố.")