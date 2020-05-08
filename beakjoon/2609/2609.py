
def getGCD(a, b):
    return getGCD(b, a % b) if b != 0 else a


a, b = map(int, input().split())

gcd = getGCD(a, b)
lcm = int(a*b/gcd)

print(gcd)
print(lcm)
