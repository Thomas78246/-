n = int(input())
prime = [0] * 2 + [1] * (n-1)

for i in range(1, n+1):
    if prime[i]==0:
        continue
    else:
        for j in range(i**2, n+1, i):
            prime[j] = 0

for i in range(1, n+1):
    if prime[i]==1 and prime[n-i]==1:
        print(i, n-i)
        break
