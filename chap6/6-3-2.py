import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split() )
c = [ input() for i in range(H) ]

for i in range(H):
  for j in range(W):
    if c[i][j] == "s":
      sy, sx = i, j
    if c[i][j] == "g":
      gy, gx = i, j

visited = [ [False] * W for i in range(H) ]

def dfs(i, j):
  visited[i][j] = True

  for i2, j2 in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
    if not (0<=i2<H and 0<=j2<W):
      continue
    if c[i2][j2] == "#":
      continue

    if not visited[i2][j2]:
      dfs(i2, j2)

dfs(sy,sx)

if visited[gy][gx]:
  print("Yes")
else:
  print("No")