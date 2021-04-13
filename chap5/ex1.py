import numpy as np 
mylist = [list(map(int, input().split())) for i in range(3)]
nmylist= np.array(mylist)
N = int(input())
li= [int(input()) for _ in range(N)]

for i in range(3):
  for j in range(3):
    for k in range(N):
      if nmylist[i][j] == li[k]:
        nmylist[i][j] = True
# print(nmylist)
bingo = False
row = np.all(nmylist == True, axis=0)
col = np.all(nmylist == True, axis=1)

if nmylist[0][0] == nmylist[1][1] == nmylist[2][2]:
  bingo = True
elif nmylist[0][2] == nmylist[1][1] == nmylist[2][0]:
  bingo = True
elif True in row:
  bingo = True
elif True in col:
  bingo = True

if bingo == True:
  print("Yes")
else:
  print("No")