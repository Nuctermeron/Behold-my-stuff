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

print("Jaka ma być długość fraktala?")
x = int(input())
t.forward(x)
frac_widly(x)