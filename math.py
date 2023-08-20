import math

def calculate_gcd(numbers):
    gcd = numbers[0]
    for i in range(1, len(numbers)):
        gcd = math.gcd(gcd, numbers[i])
    return gcd

def calculate_lcm(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = (lcm * numbers[i]) // math.gcd(lcm, numbers[i])
    return lcm

def get_numbers():
    numbers = []
    n = int(input("请输入数字的个数: "))
    for i in range(n):
        num = int(input("请输入第{}个数字: ".format(i+1)))
        numbers.append(num)
    return numbers

numbers = get_numbers()

gcd = calculate_gcd(numbers)
lcm = calculate_lcm(numbers)

print("最大公约数:", gcd)
print("最小公倍数:", lcm)
