import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=["apple","banana","camel"]
chosen_word=random.choice(word_list)

display=[]
for letter in chosen_word:
    display.append("_")
end_of_game= False
#todo - 1 : 남은 목숨 수를 추적하기 위한 'lives'라는 변수를 선언하고, 6으로 초기화하세요.
lives = 6
while not end_of_game:
    # print(stages[lives])
    guess = input("알파벳을 하나 추측해서 입력하시오. >>> ").lower()

    for i in range(len(chosen_word)):

        if chosen_word[i] == guess:

            display[i] = guess
            print(stages[lives])


        # elif chosen_word[i] != guess:
        #     lives -= 1
        #     print(f"남은 목숨은 {lives} 입니다")
        #라고 작성하시면 안됩니다.-> 알파벳을 하나 입력할 떄마다 모든 단어에서 ㅇ라파벳이 맞는지 확인하는 조건문이 실행되기 떄문이다.
        #
        #     if lives==0:
        #         print("모든 기회를 잃었습니다.")
        #         end_of_game = True

        #이상을 이유로 for 반복문 바깥에서 (즉 들여쓰기 잓용 x)guess가 chosen_word에 속하지 않는지를 확인하는 조건문은 작성하자.
        # todo - 2 : 추측한 알파벳이 chosen_word에 없으면 lives를 1 감소시키세요.
        #  lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.
    if guess not in chosen_word:
        lives-=1
        print(f"당신의 기회는 {lives}번 남았습니다.")


        if lives==0:
            print("모든 기회를 잃었습니다.")
            end_of_game = True
            print(f"정답은 {chosen_word}입니다.")
    #다 맞쳤을 때는 이렇게 판별하고, 어떻게 반복문을 종료시킬 것인가.
    # todo - 4 : 사용자가 모든 문자를 맞췄는지 확인하세요 -> 정답을 맞췄다면 "정답입니다!!:)"를 출력하세요
    if "_" not in display:
        print("정답입니다.")
        end_of_game = True


    #print(display)
    # todo - 3 : display list의 모든 요소를 결합하여 문자열로 변환하세요.
    print(" ".join(display))
    #print(stages[lives])
    # todo - 4 : 사용자가 모든 문자를 맞췄는지 확인하세요 -> 정답을 맞췄다면 "정답입니다!!:)"를 출력하세요

# 여기까지 작성했을 때 비어있는 점
#1. 로고
#2, word_list 부족
#3. 혹시 테스트 해보고 유지 보수 및 리팩토링 지점이 있는지 확인할 필요가 있음. -> 함수화





