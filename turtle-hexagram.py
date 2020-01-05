from turtle import *
shape("turtle")
col = ["yellow", "blue", "orange", "plum", "limegreen", "tomato"]

for i in range(100):
    if i % 2 == 0:
        right(120)
        for j in range(3):
            color(col[j % 3])
            forward(100)
            right(120)
            color(col[(j + 1) % 3])
            forward(200)
    else:
        left(120)
        for k in range(3):
            color(col[(k % 3) + 3])
            forward(100)
            left(120)
            color(col[((k + 1) % 3) + 3])
            forward(200)

done()
