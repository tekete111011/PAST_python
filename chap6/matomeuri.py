import copy
N = int(input())
C = list(map(int, input().split() ))
Q = int(input())

for i in range(Q):
  query = list(map(int, input().split() ))

  if query[0] == 1:
    if C[query[1]-1] >= query[2]:
      C[query[1]-1] -= query[2]
    print(C)

  elif query[0] == 2:
    hay = [ j for j in C[::2] ]
    hay = [ True if j >= query[1] else False for j in hay ]
    if all(hay):
      C = [ C[j]-query[1] if (j%2)==0 else C[j] for j in range(N) ]
    else:
      continue
    print(C)

  elif query[0] == 3:
    hay = [ True if j >= query[1] else False for j in C ]
    if all(hay):
      C = [ C[j]-query[1] for j in range(N) ]
    print(C)

print(sum(C))