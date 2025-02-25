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
# for l in range(4):
#     for _ in range(5):
#         t.penup()
#         t.forward(20)
#         t.pendown()
#         t.forward(20)
#     t.left(90)
#
# for l in range(3):
#     for _ in range(5):
#         t.penup()
#         t.forward(20)
#         t.pendown()
#         t.forward(20)
#     t.left(120)

# for _ in range(3):
#     t.forward(100)
#     t.left(120)
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
# for _ in range(5):
#     t.forward(100)
#     t.left(72)
# for _ in range(6):
#     t.forward(100)
#     t.left(60)

from turtle import Turtle, Screen
import random

t = Turtle()  # Turtle 클래스의 객체 생성, 이름은 t
screen = Screen()  # Screen 클래스의 객체생성

t.shape("turtle")
# t.color("white")
screen.bgcolor("gray")


# for i in range(1,4,1):
#     for _ in range(10):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()
#     a=(180*i)/(i+2)
#     t.left(a)

# for i in range(4):
#     for _ in range(10):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()
#     t.left(90)


def dotted_line():
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()


# 이상의 함수를 사용하여 사각형을 그린다고 가정했을 때
# for _ in range(4):
#     dotted_line()
#     t.left(90)


# def draw_figures(num):
#     for _ in range(num):
#         dotted_line()
#         t.left(360/num)


# 랜덤 객체 생성
random = random.Random()
colors = ["lawn green",
          "white",
          "pink",
          "yellow",
          "deep sky blue",
          "misty rose",
          "orange"]  # 내부에 거북이 색깔들을 요소로 하는 리스트를 완성 랜덤 모듈을 사용해서요(행맨에서 햇음)

# 1. draw_figures(num)을 정의하시오.
# 2. num이 3미만이라면 "도형을 그릴 수 없습니다." 라고 출력되고 메서드를 종료하시오,
# 3. 3이상이라면 해당 메서드가 실행될수 있도록 하시고,
# 4. 반복문을 통해 draw_figures를 호출해 삼각형부터 삼각형까지 그리는데,
# 5. 도형마다 색깔이 다를 수 있도록 작성핫.오.
# def draw_dotted_figures(num):
#     for _ in range(num):
#         dotted_line()
#         t.left(360/num)

# for i in range(3,11,1):
#     draw_figures(i)
#     chosen_color = random.choice(colors)
#     t.color(chosen_color)

# def draw_figures(num):
#     t.color(random.choice(colors))
#     if num < 3:
#         print("도형을 그릴 수 없습니다. ")
#         return         #함수에서 return 다음 아무것도 입력하지 않으면 함수 종료
#         #screen.bye()은 창이 끝남
#     for _ in range(num):
#         t.forward(100)
#         t.left(360 / num)
#
#
#
# t.speed(10)
# # draw_figures(3)
# # draw_figures(4)
# # draw_figures(1)
# for i in range(11):
#     draw_figures(i)


# for i in range(num):
#     draw_figures(i)
#     chosen_color = random.choice(colors)
#     t.color(chosen_color)


'''
    .heading() 메서드:
        거북이가 바라보는 방향을 나타내는 속성으로 도(degree)단위로 나타남.
        해당메서드는 콘솔창에 float형태로 출력됩니다.
        0도 : 동
        90도 : 북
        180도 : 서
        270도 : 남

    .setheading() 메서드 :
        특정 각도로 거북이를 회전시키는 메서드
    .circle() 메서드:
        거북이가 원을 그리는 메서드

'''


# t. forward(100)
# print(t.heading())
# t. right(90)
# print(t.heading())
# for _ in range(10):
#     t.circle(100)
# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(t.heading()+10)
# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(t.heading()+10)
# t.circle(100)
# for _ in range(360//30):
#     t.circle(100)
#     t.color(random.choice(colors))
#     t.setheading(t.heading()+30)
# 이상의 네 출의 코드를 응용하여 draw_spriograph(size_of_gap)로 함수화하시오
def draw_spriograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        t.circle(100)
        t.color(random.choice(colors))
        t.setheading(t.heading() + size_of_gap)


t.speed(0)
draw_spriograph(2)

screen.exitonclick()