import turtle

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.delay(0)
# turtle settings
leo = turtle.Turtle()
leo.color('green')
leo.pensize(3)
leo.speed(150)
leo.penup()
leo.setpos(WIDTH // 6, -HEIGHT // 4 - 20)
leo.pendown()
leo.color('green')
# l-system settings
gens = 6
axiom = 'XY'
chr_1, rule_1 = 'F', 'FF'
chr_2, rule_2 = 'X', 'F[+X]F[-X]+X'
step = 6
angle = 35
stack = []


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else 
    rule_2 if chr == chr_2 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

axiom = get_result(gens, axiom)
leo.left(90)
for chr in axiom:
    if chr == chr_1:
        leo.forward(step)
    elif chr == '+':
        leo.right(angle)
    elif chr == '-':
        leo.left(angle)
    elif chr == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_))
    elif chr == ']':
        angle_, pos_= stack.pop()
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()import turtle

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.delay(0)
# turtle settings
leo = turtle.Turtle()
leo.color('green')
leo.pensize(3)
leo.speed(150)
leo.penup()
leo.setpos(WIDTH // 6, -HEIGHT // 4 - 20)
leo.pendown()
leo.color('green')
# l-system settings
gens = 6
axiom = 'XY'
chr_1, rule_1 = 'F', 'FF'
chr_2, rule_2 = 'X', 'F[+X]F[-X]+X'
step = 6
angle = 35
stack = []


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else 
    rule_2 if chr == chr_2 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

axiom = get_result(gens, axiom)
leo.left(90)
for chr in axiom:
    if chr == chr_1:
        leo.forward(step)
    elif chr == '+':
        leo.right(angle)
    elif chr == '-':
        leo.left(angle)
    elif chr == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_))
    elif chr == ']':
        angle_, pos_= stack.pop()
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()
