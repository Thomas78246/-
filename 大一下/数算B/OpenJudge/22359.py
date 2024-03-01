n = int(input())
prime = [0]*2 + [1]*(n-1)
for i in range(n+1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = 0
for i in range(n):
    if prime[i] and prime[n-i]:
        a = i
        b = n - i
        break
print(a, b)
