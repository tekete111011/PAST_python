N = int(input())
C = list(map(int, input().split() ))
Q = int(input())

sell = 0
s = 0
z = 0
min_s_c = 10**10
min_z_c = 10**10

for i in range(N):
  if (i%2)==0:
    min_s_c = min(min_s_c,C[i])
  else:
    min_z_c = min(min_z_c,C[i])

for i in range(Q):
  query = list(map(int, input().split() ))

  if query[0] == 1:
    x, a = query[1]-1, query[2]

    if (x%2)==0:
      card_x = C[x] - s - z
    else:
      card_x = C[x] - z

    if card_x >= a:
      C[x] -= a
      sell += a
      if x % 2 == 0:
          min_s_c = min(C[x], min_s_c)
      else:
          min_z_c = min(C[x], min_z_c)

  elif query[0] == 2:
    a = query[1]

    if min_s_c - s -z >= a:
      s += a

  elif query[0] == 3:
    a = query[1]

    if min(min_s_c - s - z, min_z_c - z) >= a:
      z += a

sell += sum([ s for i in range(N) if (i%2)==0 ])
sell += z * N
# sell += s * math.ceil( N / 2 ) + z * N
print(sell)