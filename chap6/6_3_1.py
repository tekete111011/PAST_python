from collections import deque

R, C = map(int, input().split() )
sy, sx = map(int, input().split() )
gy, gx = map(int, input().split() )
S = [ input() for i in range(R) ]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

dist = [ [-1]*C for i in range(R) ]

Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

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