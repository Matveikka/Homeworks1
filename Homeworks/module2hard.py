def num_to_password(num: int) -> str:
    password = ""
    if num % 2 == 0:
        iter = (num // 2) - 1
    else:
        iter = num // 2
    for i in range(1, iter + 1):
        j = num - i
        password += str(i)
        password += str(j)
    return password
def multiples_to_password(num: int):
    password = ""
    num = num
    for k in range(3, num):
        if num % k == 0:
            print(f"Найдено кратное число для {num}: {k}")
            password += num_to_password(k)
    return password
a = int(input())
result = num_to_password(a)
result += multiples_to_password(a)
print(result)


