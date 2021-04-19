n, l = list(map(int, input().split() ))
x = list(map(int, input().split() ))
t1, t2, t3 = list(map(int, input().split() ))

#h = [ True if j in x else False for j in range(l+1) ] TLEの原因
h = [False] * (l+1)
for i in x:
  h[i] = True

cost = [10**100] * (l+1)

cost[0] = 0

for i in range(1, l+1):
  cost[i] = min(cost[i], cost[i-1] + t1)

  if i >= 2:
    cost[i] = min(cost[i], cost[i-2] + t1 + t2)

  if i >= 4:
    cost[i] = min(cost[i], cost[i-4] + t1 + 3*t2)

  if h[i]:
    cost[i] += t3

ans = cost[l]
for i in [l-3, l-2, l-1]:
  if i >= 0:
    ans = min(ans, cost[i] + t1//2 + t2*(2*(l-i)-1)//2 )

print(ans)