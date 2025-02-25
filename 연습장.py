class NegativeNumIndexError(Exception):
    pass
my_list=[10,20,30,40,50]
try:
    index_num=input("인덱스 넘버를 입력하세요>>>")
    index_num=int(index_num)
    if index_num<0:
        raise NegativeNumIndexError("마이너스 인덱스는 적용하지 않습니다.")
    chosen_element=my_list[index_num]
except NegativeNumIndexError as e:
    print("정수만 입력할 수 있습니다.")
    print(e)
except ValueError as e:
    print("List의 범위를 벗어났습니다.")
    print(e)
except TypeError as e:
    print("자료형이 잘못 입력되었숩니다.")
    print(e)
except Exception as e:
    print("예측할 수 없는 예외가 발생했습니다.")
    print(e)
else:
    print(f"{index_num} 위치에 있는 값은 {chosen_element}입니다.")
finally:
    print("프로그램이 종료되었습니다.")
