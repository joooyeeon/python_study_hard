#turtle이라는 모듈을 사용할건데, Turtle, Screen, 클래스를 import 할겁니다
from turtle import Turtle, Screen
t=Turtle() # Turtle 클래스의 객체 생성, 이름은 t
screen = Screen()#Screen 클래스의 객체생성

t.shape("turtle")
t.color("white")
screen.bgcolor("gray")

# for _ in range(10): #그냥 반복을 10번 라는 거고 변수를 사용하지 않앗기 때문에 _를 썼습니당. (i나 n이 아니더라도)
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)
#  정삼각형 그리기
# for _ in range(3):
#     t.forward(100)
#     t.left(120)
for l in range(4):
    for _ in range(5):
        t.penup()
        t.forward(20)
        t.pendown()
        t.forward(20)
    t.left(90)


screen.exitonclick()