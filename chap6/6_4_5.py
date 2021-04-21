n = int(input())
ps = [0] + list(map(int, input().split() ))

p = sum(ps)

exist = [ [False]*(p+1) for _ in range(n+1) ]
exist[0][0] = True

for i in range(1,n+1):
  for j in range(p+1):
    if exist[i][j-1]:
      exist[i][j] = True
    elif ps[i] <= j and exist[i-1][j-ps[i]]:
      exist[i][j] = True

print(exist[n].count(True))