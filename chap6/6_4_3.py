import sys
sys.setrecursionlimit(100000)

n = int(input())
h = list(map(int, input().split() ))

cost = [0] * n
done = [False] * n

def rec(i):
  if done[i]:
    return cost[i]

  if i == 0:
    cost[i] = 0

  elif i == 1:
    cost[i] = rec(0) + abs(h[1] - h[0])

  else:
    cost[i] = min(rec(i) + abs(h[i] - h[i-1]), rec(i-2) + abs(h[i] - h[i-2]))

  done[i] = True
  return cost[i]

print(rec(n-1))