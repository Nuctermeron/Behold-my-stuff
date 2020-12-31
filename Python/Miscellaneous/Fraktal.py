import turtle
t = turtle.Turtle()
t.speed("fastest")
def frac_widly(x):
  if x<=1:
    return
  t.left(90)
  t.forward(x)
  t.right(90)
  t.forward(x)
  frac_widly(x/3)
  # cofnij się
  t.backward(x)
  t.right(90)
  t.forward(x)
  # rysuj środkową część wideł (rys. 3)
  t.left(90)
  t.forward(x)
  frac_widly(x/3)
  # cofnij się
  t.backward(x)
  # rysuj prawą część wideł (rys. 4)
  t.right(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  frac_widly(x/3)
  # cofnij się do punktu początkowego i obróć się
  # w kierunku początkowym (rys. 5)
  t.backward(x)
  t.left(90)
  t.forward(x)
  t.right(90)

#ćw1
t2 = turtle.Turtle()
t2.speed("fastest")
t2.color("Pink")

def triangle(x):
  t2.forward(x)
  t2.left(120)
  t2.forward(x)
  t2.left(120)
  t2.forward(x)


def infi_square(x):
  t3 = turtle.Turtle()
  t3.speed("fastest")
  if x<=1:
    return
  for i in range(4):
    t3.forward(x)
    t3.left(90)
  infi_square(x-5)

# print("Jaka ma być długość fraktala?")
# x = int(input())
# t.forward(x)
# frac_widly(x)

# print("Jaka ma być długość trójkąta?")
# x = int(input())
# triangle(x)
  
# print("Jaka ma być długość kwadrata?")
# x = int(input())
# infi_square(x)

