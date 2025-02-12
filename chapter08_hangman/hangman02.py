import random


word_list=["apple","banana","camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
guess=input("알파벳을 하나 추측해서 입력하시오. >>> ").lower()

#todo-1: 비어있는 list인 display를 만드시오.
# chosen_word의 각 문자 개수마다 "_"를 추가하시오. 예를 들어 chosen_word="apple"이라면,
# display=["_","_","_","_","_"]이 되어야합니다. 즉 , chosen_word의 문자 개수만큼 "_"가 생깁니다.
display=[]
# for _ in range(len(chosen_word)):         #  변수가 사용되지 않으므로 i 가아니라 _ 로 ㅁ엿,
#     display.append("_")
# print(display)
# 형성된 for 문
for letter in chosen_word:
    display.append("_")
print(display)
#todo-2: chosen_word의 각 문자들을 반복시키세여. 만약 그 위피의 문자가 guess와 일치하면, 해당 위치의 display에서 해당문자를
# 공개하시오, ex) 사용자가 "p"를 입력했고, chosen_word가 "apple"이라면 display=['_','p','p','_','_']로 바꿔야됨
 # 한트:
 #list의 각 요소를 재 대입하는 방법
 # numbers=[1,2,3,4,5]
 # print(numbers)
 # numbers[0]=100
 # print(numbers)


for i in range(len(chosen_word)):
    if chosen_word[i]==guess:
        display[i]=guess
    #else는 안써도 됨 틀ㄹ렷을떄의 지시사항이 없는 상황
print(display)


