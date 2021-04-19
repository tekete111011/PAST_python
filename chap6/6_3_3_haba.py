from collections import deque

N = int(input())

Q = deque()
Q.append([sy, sx])

while len(Q) > 0:
  i, j = Q.popleft()

  for i2, j2 in [ [i,j-1], [i, j+1], [i-1,j], [i+1,j] ]:
    if not (0<=i2<R and 0<=j2<C):
      continue
    if S[i][j] == "#":
      continue
    if dist[i2][j2] == -1:
      dist[i2][j2] = dist[i][j] + 1
      Q.append([i2, j2])

print(dist[gy][gx])
print(dist)