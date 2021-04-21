N, M = map(int, input().split() )
A = [ input() for i in range(N) ]

group = [ [] for _ in range(11) ]
for i in range(N):
  for j in range(M):
    if A[i][j] == "S":
      n = 0
    elif A[i][j] == "G":
      n = 10
    else:
      n = int(A[i][j])
    group[n].append([i, j])

# print(group)
cost = [ [10**100] * M for _ in range(N) ]

si, sj = group[0][0]
gi, gj = group[10][0]

cost[si][sj] = 0

for n in range(1, 11):
  for i, j in group[n]:
    for i2, j2 in group[n-1]:
      cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i-i2) + abs(j-j2) )

ans = cost[gi][gj]
if ans == 10**100:
  ans = -1
print(ans)