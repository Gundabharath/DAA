def prime_num(n,i=2):
    if n<=2:
        return 2
    elif n % i == 0:
        return False
    elif i * i == 0:
        return True
    return prime_num(n,i+1)
n = int(input())
if prime_num(n):
    ptint("prime num")
else:
    print("Not a prime num")
