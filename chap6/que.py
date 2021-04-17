from collections import deque

N = int(input())
E = [ False * N for i in range(N) ]
s = int(input())

visited = [False] * N

Q = deque()
Q.append(s)
visited[s] = True

while len(Q) > 0:
  i = Q.popleft()
  for j in E[i]:
    if not visited[j]:
      visited[j] = True
      Q.append(j)