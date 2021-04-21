n, w = list(map(int, input().split() ))

ws = [0]
vs = [0]
for i in range(n):
  W, V = map(int, input().split() )
  ws.append(W)
  vs.append(V)

value = [ [-10**10]*(w+1) for i in range(n+1) ]
value[0][0] = 0

for i in range(1, n+1):
  for j in range(w+1):
    value[i][j] = max(value[i][j], value[i-1][j])

    if j - ws[j] > 0:
      value[i][j] = max(value[i][j], value[i-1][j-ws[i]] + vs[i])

print(max(value[n]))