N, Q = map(int, input().split())

graph = [ [False]*N for i in range(N) ]

for i in range(Q):
  s = list(map(int, input().split() ))
  n = s[0]

  if n == 1:
    a, b = s[1]-1, s[2]-1
    graph[a][b] = True

  elif n == 2:
    a = s[1]-1
    for j in range(N):
      if graph[j][a]:
        graph[a][j] = True
  
  elif n == 3:
    a = s[1]-1
    to_follow = []
    for j in range(N):
      if graph[a][j]:
        for k in range(N):
          if graph[j][k] and k!=a:
            to_follow.append(k)

    for j in to_follow:
      graph[a][j] = True

graph_new = [ [ 'Y' if tx else 'N' for tx in txi] for txi in graph ]

[ print("".join(tx)) for tx in graph_new ]