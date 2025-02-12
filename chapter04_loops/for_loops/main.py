'''
1. for 반ㅂㄱ문의 기본개념:
    정해진 구간 혹은 집합 내의 요소드을 순서대로 꺼내면서 반복 작업을 수행.
    예를 들어 아까 전에 문자열의 index 개념을 학습했습니다.
    String의 경우에는 문자열의 문자 개수만큼 반복이 진행된다고 해석할 수 있습니다.
    Collection을 기반으로 반복문을 배울 수도 있지만 이건 다음 시간에 할 예정입니다.

        1) 숫자 범위를 이용한 반복
        range(): 몇번 반복할 것인가를 지정화는 함수 -> 툭하  for문과 연계

'''
#1부터 10까지를 출력하는 while 바ㅣㄴ복ㅂ문
# n=1
# while n<11:
#     print(n)
#     n+=1

#1부터 10까지를 출력하는 for 반복문
# for i in range(11):                 #현재 상황에서의 반복횟수는 11번
#     print(i)
#
# print()
#
# for i in range(10):                #얘는 반복횟수 10번인데, 여기서 중요한 것은 시작 지점이 0부터라는 점
#     print(i+1)

'''
                range()함수의 응용:
                    range((시작값),종료값,(증감값))
                    
                    시작값: 생략 가능, 생략할 경우에 0부터 시작
                    종료값: 명시하지 않으면 끝까지 진행
                    증감값: 생략 가능, 생략할 경우에 1씩 증가 -> index에서의 slicing 개념과 유사
    
for 반복문
형식:
for i(아무거나 사용가능) in range( 시작값, 종료값, 증감값):
    반복실행문
'''

# for i in range(1,10,1):         # 종료값이 10인데 1부터 시작해도 9까지 나타납니다.
#     print (i)                   # 종료값이 바로 앞인데 출력이 이루어짐을 확인할 수 있습니다.

'''
    2) 문자열을 이용한 반복
        문자열의 경우 []를 통해 내부에 인덱스 넘버를 명시할 수 있다는 것을 확인했습니다.
        그래서 in range()를 사용하는 방법 및 형상된 for문을 사용하는 방법을 통해
        문자를 하나씫 추출 할 수 있습니다.
'''

name="parkjooyeon"
#(1) in range()를 이용헤 문자를 추출하는 방법
# for i in range(len(name)):          #len(): () 안에 들어가는 요소의 길이를 반환하는 함수
#     print(name[i])

#(2)enhanced for loop를 통한 방식
# for letter in name:      #name이라는 string에서 각 문자 하나씩을 뽑아  letter에 대입함.
#     print(letter)

#첫번째 반복의 경우
# letter=name[0]
# print(letter)
# #두번째 반복
# letter=name[1]
# print(letter)
# #...
# letter=name[10]
# print(letter)

'''
 대부분의 경우 반복문을 사용하게 되면 반복 대상이 되는 객체는 복수형의 변수명을 지닙니다.
 ex)numbers=[1,2,3,4,5]
 
 for number in numbers:
    print(number)
    
형성된 for loop의 형식:
for 변수 in 반복대상객체:
    반복실행문
    
반복대상객체(iterable):내부에 요소가 다수 드어가있어 반복적으로 요소의 데이터를 다룰 수 있는 객체
ex)str,list,tuple,set,dict->현재 저희는 str만 기준으로 수업중

주의사항:
    if 조건문과 마찬가지로 들여쓰기 (indented writing(이 매우중요함
    
    문자열에서 특정 문자의 개수세기
'''
# count_a=0
# count_letters=0
# for letter in "banana":
#     if letter=="a":
#         count_a+=1
#     print(letter)
#     count_letters+=1
# print(f"a의 개수 : {count_a }")
# print(f"전체 문자 개수: {count_letters}")
# print(f"전체 문자 개수: {len("banana" )}")

count_letters=0
for letter in "banana":
    print(letter)
    count_letters += 1
print(f"전체 문자 개수: {count_letters}")


'''
reeborg's world hurdl#1
for i in range(6):
 move()
 turn_left()
 move()
 turn_left()
 turn_left()
 turn_left()
 move()
 turn_left()
 turn_left()
 turn_left()
 move()
 turn_left()

n=0
while n>6:
 move()
 turn_left()
 move()
 turn_left()
 turn_left()
 turn_left()
 move()
 turn_left()
 turn_left()
 turn_left()
 move()
 turn_left()
 n+=1
 
 
Hurlde 2.
def turn_right():
    for _ in range(3):
        turn_left()


def jump():
 move()
 turn_left()
 move()
 turn_right()
 move()
 turn_right()
 move()
 turn_left()
  
while not at_goal():
    jump()

    
Hurdle#3
def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn left() 

while not at_goal():
    
    if wall_in_front():
        jump()
    else:
        move()
        
        
        
Hurdle#4
def turn_right():
    for _ in range(3):
        turn_left()

def jump(): # 힌 칸의 장애물만 넘을 수 있음
    turn_left()
    while  wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
        
        
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
        
Maze
오른쪽만 막혀ㅇ있을땐 앞으로 막어 앞
오른쪽과 앞이 막혀잇을 때 완쪽으로 
오른쪽  비어있으면  오른쪽ㅇ,ㄹ 돌기 
def turn_right():
    for _ in range(3):
        turn_left()
        
        
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
        
    elif right_is_clear():
        turn_right()
        move()
   

'''