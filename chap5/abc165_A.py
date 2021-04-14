K = int(input())
A, B= map(int, input().split())
ans = "T"
k = K
i = 1

while k <= 1000:
  if A<=k<=B:
    ans = True
    break
  else:
    ans = False
  i += 1
  k = i * K
  # print(k)
  

if ans == True:
  print("OK")
elif ans == False:
  print("NG")
else:
  print("Error")