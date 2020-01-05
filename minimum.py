x = input()

smin = 9
count = [0] * 10

for i in range(len(x)):
    if int(x[i]) != 0:
        smin = min(smin, int(x[i]))
    count[int(x[i])] += 1

if count[0] != len(x):
    mn = str(smin)
    count[smin] -= 1

    for i in range(10):
      mn += str(i) * count[i]

    print(mn)

else: print(0)
