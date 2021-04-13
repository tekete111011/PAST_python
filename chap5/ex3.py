import copy
N = int(input())
a = [list(input()) for i in range(N)]
b = []

while a != b:
  b = copy.deepcopy(a)
  for i in range(N-1):
    for j in range(1,2*N-2):
      # if j == 0 and a[i][j] != "." and (a[i+1][j]=="X" or a[i+1][j+1]=="X"):
      #   a[i][j] = "X"
      # elif j == 2*N-1 and a[i][j] != "." and (a[i+1][j-1]=="X" or a[i+1][j]=="X"):
      #   a[i][j] = "X"
      if a[i][j] != "." and (a[i+1][j-1]=="X" or a[i+1][j]=="X" or a[i+1][j+1]=="X"):
        a[i][j] = "X"

for k in range(N):
  print("".join(a[k]))