
def gcd(n1: int, n2: int) -> int:
    # Return the gcd of two integers

    result: int = 1 # Initial gcd is 1
    k: int = 2 # Possible gcd is 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            result = k # Update gcd
    k += 1
    return result # Return gcd

def reverse(l: list[int]) -> list[int]:
    result: list[int] = [0] * len(l)
    for i in range(0, len(l)):
        result[i] = l[len(l) - 1 - i]
    return result