n = input()
na= n.count("a")
nb= n.count("b")
nc= n.count("c")

ans= max(na,nb,nc)
if na == ans:
  print("a")
elif nb == ans:
  print("b")
else:
  print("c")