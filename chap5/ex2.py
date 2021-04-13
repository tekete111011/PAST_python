import numpy as np
mylist = np.array([list(map(int, input().split())) for i in range(3)])

a = np.array([[0]*3 for i in range(4)])
for i in range(2):
  a[i] = mylist[1+i]-mylist[i]
  a[i+2] = mylist[:, 1+i] - mylist[:, i]
#print(a)

ans = True
for i in range(4):
  if a[i, 0]!=a[i, 2] or a[i, 0]!=a[i, 1] or a[i, 1]!=a[i, 2]:
    ans = False
  #print(a[i, 1])

if ans == True:
  print("Yes")
else:
  print("No")