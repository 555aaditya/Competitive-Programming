y, w = map(int, input().split())
numerator = 6 - max(y, w) + 1
denominator = 6
gcd = 1
for i in range(1, min(numerator, denominator) + 1):
    if numerator % i == 0 and denominator % i == 0:
        gcd = i
print(f"{numerator // gcd}/{denominator // gcd}")