from turtle import *
shape("turtle")
col1 = ["orange","limegreen","plum","tomato","blue"]
for j in range(2):
    for i in range(5):
        color(col1[i])
        circle(100)
        left(36)
done()
