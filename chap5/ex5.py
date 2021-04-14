N = int(input())
count = 0
i = 1
n = 0

while N != n:
  ks = list(str(i))
  ans = all([ j == ks[0] for j in ks[1:]])
  if ans == True:
    n += 1
  i += 1

print(i-1)