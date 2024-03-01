n = int(input())
org = input()
m = len(org) // n
org_1 = [''.join(reversed(org[n*i:n*(i+1)])) if i%2==1 else org[n*i:n*(i+1)] for i in range(m)]
# print(n, m, len(org))
# # print(org)
# # print(org_1)
trans = ''
for i in range(n):
    for j in range(m):
        try:
            trans += org_1[j][i]
        except IndexError:
            print(i, j)
print(trans)
