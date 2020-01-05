from turtle import *
shape("turtle")
col1 = ["yellow","blue"]
col2 = ["orange","plum"]
col3 = "limegreen"
col4 = "tomato"
for i in range(100):
    for j in range(2):
        color(col1[j])
        forward(200)
        left(120)
    color(col3)
    forward(400/3)
    left(60)
    color(col4)
    forward(400/3)
    left(120)
    for k in range(2):
        color(col2[k])
        forward(200)
        left(120)
    color(col4)
    forward(200/3)
    right(60)
    color(col3)
    forward(200/3)
    left(120)
done()
