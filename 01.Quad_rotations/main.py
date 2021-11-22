import turtle

def pic(a):
  for i in range(4):
    joe.color(colors[i])
    joe.forward(a)
    joe.left(90)

colors = ['red', 'brown', 'green', 'blue']
joe = turtle.Turtle()
joe.speed(1000)

dlina = 40
for i in range(1000):
  pic(dlina)
  joe.right(5)
  dlina = dlina + 1
