'''
지시사항

사용자에게 전체 음식값($), 몇%의 팁을 낼 것인지, 인원수를 입력받을 예정임

실행 예

음식 가격은 얼마입니까? >>> $200
몇 퍼센트의 팁을 내실 예정입니까, 10, 12, 15% 중에서 선택하시오.>>> 10
몇 명의 인원이 나누어 내나요?>>> 5

당신이 내야할 전체 음식 금액은 $44.0 달러입니다.
'''

#percent가 10, 12,15중 화나니까 얜를 0.1, 0.12, 0.15로 바꿀 필요거 잇음
#food오ㅓㅣ ㅔpercent를 가지고ㅓ 어떻게 잘연산해서 전페 음식값을 산풀
#전체 음ㅅ긱밧에서  people 나누삼
#맨마지막에 플략므느,ㄹㅇㄹ f-string을 작성

food=input("음식 가격은 얼마입니까? >>> $")
food=float(food)
percent=input("몇 퍼센트(%)의 팁을 내실 예정입니까?>>>")
percent=float(percent)
percent=percent/100
percent_round=float(percent)
people=int(input("몇 명의 인원이 나누어 내나요?>>> "))
people=int(people)
mon=food*(1+percent_round)
mon=float(mon)
fffff=mon/people
fffff=round(fffff,2)
print(f"당신이 내야할 전체 음식 금액은 ${fffff}달러입니다.")


'''
percent=percent/100
tip=food*percent
total_price=food+tip
price_person=total_price/people
price_person=round(price_person,2)
print(f"당신이 내야할 전체 음식 금액은 $ {price_person}입니다긔")
'''
'''
food=float(input("음식 가격은 얼마입니까"))
percent=float(input("몇 퍼센트(%)의 팁을 내실 예정입니까?"))/100
people=int(input("몊 명입니까"))
print(f"금액은 {round((food*(1+[percent))/people,2)}입니다.")
print(f:당신이 내야할 전체 금액은 {((food*(1+percent))/people):.2f}입니다.")
#47번 라인의 경우는 round()함수와 달리 어떤 상황에서도 소수점 둘째자리까지 표기되도록 강제하는 코드
'''
