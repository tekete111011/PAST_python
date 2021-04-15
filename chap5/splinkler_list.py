N, M, Q = map(int, input().split())
graph = [ [] for i in range(N)]
for i in range(M):
  u, v = map(int, input().split())
  
  u -= 1
  v -= 1

  graph[u].append(v)
  graph[v].append(u)

cs = list(map(int, input().split()))

for i in range(Q):
  query = list(map(int, input().split()))
  x = query[1]-1
  print(cs[x])

  if query[0] == 1:
    for j in graph[x]:
      cs[j] = cs[x]

  if query[0] == 2:
    cs[x] = query[2]