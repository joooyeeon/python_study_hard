'''
1. 생성자(Constructor)
'''
from idlelib.run import manage_socket

# 클래스 정의
# class Candy:
#     def set_info(self,shape, color):
#         self.shape=shape
#         self.color=color
#
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")
# #객체 생성
# satang=Candy()
# satang.set_info("구형","갈색")
# satang.display_info()
'''
    satang이라는 인스턴스는 생성된 '이후'에 set_info() 메서드를 호출하여 "구형"모양의,"갈색"이라는 속성(attribute)를 갖게됩니다.

    satang 인스턴스의 생성과정
        1. 값이 없는(속성에 값이 대입되어 있지 않은) 인스턴스를 생성
        2. 값을 저장할 수 있는 메서드 호출
    
    그렇다면 처음부터 같이 있는 인스턴스를 생성하면 코드라인이 줄어들지 않을까.
    이에 대한 해답이 생성자라는 개념이고,
    C/java의 경우의 생성자는 클래스명과 동일한데, 또 python만 이상한 방식으로 만듭니다.
    -> __init__()라는 메서드
    
    __init__(): 메서드(생성자) 는 인스턴스가 생성될 때, '자동으로호출'되기 때문에 인스톤스 변수의
    '초기화'용도로 사용, 즉 값이 있는 인스턴스를 생성할 수 있다는 의미입니다.
    '객체 생성과 동시에' 생성자가 호출됨-> 초기값을 작성할 때 사용한다는 의미
    
    형식:
    
class 클래스명:
    def __init__(self,shape,color):
    self.shape = shape
    self.color = color
'''

# class Candy2():
#     #생성자 정의
#     def __init__(self,shape,color):
#         self.shape=shape
#         self.color=color
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고 색깔은 {self.color}입니다.")
#
#     satang2=Candy2("정육면체","흰색") # 이부분에서 차이가 발견됩니다.
#     satang2.display_info()
'''
    이상에서 주목해야 할 점은 satang 인스턴스의 satang2 인스턴스의 생성 방식의 차이입니다.
    
    2. 소멸자(Destructor)
        인스턴스가 생성될 때 자동으로 생성되는 생성자와 마찬가지로 인스턴ㅅ흐가 소멸 될 때 로툴되는 메서드
        이를 소멸자라고 하며, 소멸자를 정의하는 메서드는 __del()__
        
'''
    # class Sample:
    #
    #     #생성자 정의
    #     def __init__(self):
    #         print(f"인스턴스가 생성되었습니다.")
    #     def __del__(self):
    #         print(f"인스턴스가 소멸되었습니다.")
    #
    # #객체 생성
    # sample=Sample()
    # del sample          #DEL  객체명으로 소멸자를 원하는 시기에 호출 할수 있음-> 예를 들어 일단 객체 소멸 시킴
    # #여기 부분에 추가적인 로직을 작성하여 더 프로그램이 진행된 후에 프로구래무 전체 종료가 이루ㅇ어지ㄹ 수 있음
    # print("프로그램이 종료되었습니다.")
'''
기본 예제
생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오,

지시사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info()메서드를  정의할것

main 단계 코드
usb=USB(64)
usb.get_info()

실행 예
64GB USB
'''
#1번 지시사항
# class USB():
#     #2번 지시사항
#     def __init__(self,capacity):
#         self.capacity=capacity
#
#     #3번 지시사항
#     def get_info(self):
#         print(f"{self.capacity}GB USB")
# #객체 생성 밒 get_info()메서드 호출
# usb=USB(64)
# usb.get_info()

'''
생성자와 소멸자를 이용하여 서비스 안내 메세지를 출력하는 프로그램을 작성하시오,
class Service를 정의하고, 생성자를 통해 배개변수를 service로 받고, print()메서드를 생성자와 소멸자 내에 작성하시오.
main 단계에서의 작성
s=Service("길 안내")
del s

실행예 
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.
'''
# class Service():
#     def __init__(self,service):
#         self.service=service
#         print(f"{self.service} Service가 시작되었습니다.")
#
#     def __del__(self):
#         print(f"{self.service} Service가 종료되었습니다.")
#
# s=Service("길 안내")
# #del s          # 종료전에 모든 객체가 소멸됨.
# print("프로그램이 종료되는 시점")
# del s
'''
응용 예제

1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하싯오,

지시 사항

1. 다음과 같은 방법으로 man 과 woman 인스턴스를 생성하시오,
man=Person("James")
woman=Person("emily")
2. man과 woman 인스턴스가 생성되며ㅑㄴ 다음과 같은 메세지를 출력할 수 있도록 작성하시ㅗㅇ
james is born.
emily is born

3. 다음과 같은 방법으로 man 인스턴스를 삭제핫.어
del man

4. 인스턴스가 삭제되면 다음과 같은 메세지를 출력할 수 있도ㅠ록 작성핫오
james is dead.
'''
class Person():
     def __init__(self,name):
         self.name=name
         print(f"{self.name} is born")


     def __del__(self):
         print(f"{self.name} is dead.")

man=Person("James")
woman=Person("emily")
del man
print("프로그램이 종료됨.")

'''
예제 1.
학생들의 성적을 관리하는  Student 클래스를 작성하시오. 이 클래스는 
학생의 이름, 학번, 성적을 인스턴스 변수로 갖습니다.

지시사항
1) Student 클래스를 정의하고 생성자를 통해 name, student_id, grade를 초기화하시오,
2) 학생의 프로필을 출력하는 인스턴스 메서드 print_grade()를 작성하시오, (call1()타입으로 : 매개변수 X, 리턴X)
3)ㅜ 학생의 성적을 변경할 수 있는 인스턴스 메서드 set_grade()를 작성하시오
    -> '이 부분이 고민해볼만한 요소임//set_info()메서드를 검색해보새요 ctrl+shift+f 눌러서 
4) 세 명의 학생 인스턴스를 생성하고, 각 학생의 정보를 출력한 다음,
    성적을 변경하고 다시 출력하시오
    
    student1=student("김철수",20250001,"A")
    student2=student("이영희",20250002,"B")
    student3=student("박민지",20250003,"C")
    실행 예
    
    학생 아름: 김펄수
    학번 : 20250001
    성젃 : A
    
    student2/student3도 출력하시오
    
    이후 student 1 성적을 A+ / student2는 A/ student3은 B+읫 성적을 변경하고
    다시 print_profile을 적용하여 출력하삼
'''

class Student():
    def __init__(self,name,student_id,grade):
        self.name=name
        self.student_id=student_id
        self.grade=grade
    def print_grade(self,student):
        self.student=student

student1=student("김철수",20250001,"A")
student2=student("이영희",20250002,"B")
student3=student("박민지",20250003,"C")