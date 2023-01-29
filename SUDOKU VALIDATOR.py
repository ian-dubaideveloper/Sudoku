import numpy as np

l = []
K = 0
for i in range(9):
    t = []
    for j in input().split():
        n = int(j)
        t += (n,)
    l += (t,)
l = np.array(l)
for i in range(3):
    subgrid = l[i * 3 : i * 3 + 3, 0:3]
    t = "".join("".join(str(k) for k in f) for f in subgrid)
    if len(set(t)) != 9:
        K = 1

    subgrid = l[i * 3 : i * 3 + 3, 3:6]
    t = "".join("".join(str(k) for k in f) for f in subgrid)
    if len(set(t)) != 9:
        K = 1

    subgrid = l[i * 3 : i * 3 + 3, 6:9]
    t = "".join("".join(str(k) for k in f) for f in subgrid)
    if len(set(t)) != 9:
        K = 1
for i, *k in zip(l, *l):
    if len(set(i)) + len(set(k)) != 18:
        K = 1


print("false" if k else "true")
