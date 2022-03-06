# 만약 3,000원 이상의 돈을 갖고 있으면 택시를 타고 그렇지 않으면 걸어 가라.

money = 2000
if money > 3000:
    print('택시 타라 ㅋ')
else:
    print('걸어가라 짜샤')

# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."

money = 2000
card = True # 굳이 True로 하지않고 참을 의미하는 1로 표현해도 된다. 거짓은 0으로 표현!
if money >= 3000 | card:
    print('택시')
else:
    print("걸어가라")


# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."

pocket = ['paper', 'cellphone', 'money'] # x in s, x not in s 형식 : x가 s안에 있는가? 리스트, 튜플, 문자열 모두 가능.
if 'money' in pocket:
    print("택시를 타고가라")
else:
    print("걸어 가라")

# ['paper', 'cellphone', 'money'] 리스트 안에 'money'가 있으므로 'money' in pocket은 참이 된다. 따라서 if문 다음 문장이 수행된다.


# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')
# 아무런 결괏값을 도출하지 않는데, 그 이유는 pass가 수행되었기 때문.


# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라."

pocket = ['paper','headphone']
card = True
if 'money' in pocket:
    print('택시')
else:
    if card:
        print('택시')
    else:
        print('걸어가라') # elif를 사용하지 않고 if 와 else로만 만든 코드


# 다중 조건 판단을 가능하게 하는 elif. elif는 이전 조건문이 거짓일 때 수행된다. 개수에 제한없이 사용가능.

pocket = ['paper', 'headphone']
card = True
if 'money' in pocket:
    print('택시')
elif card:
    print('택시')
else:
    print('걸어가라')




# while 반복문 : 반복해서 문장을 수행해야 할 경우 사용.

# 열 번 찍어 안 넘어가는 나무 없다?

treehit = 0  # 0부터 시작한다는 뜻
while treehit < 10: # while문의 조건 - treehit가 10보다 작은 동안에 while문 안의 문장을 계속 수행한다.
    treehit = treehit + 1 # treehit의 값이 계속 1씩 증가함.
    print('나무를 %d번 찍었습니다.' % treehit) # 왜 treehit이냐면, 72줄에 treehit이 treehit +1 이라는 숫자이기 때문.
    if treehit == 10: # treehit이 10이 되면 나무가 넘어간다는 출력, 그 때까지 계속 반복한다.
        print('나무 넘어갑니다')


#  1부터 10까지 홀수만 출력
a = 0 # 0부터 시작해서
while a < 10:
    a = a + 1
    if a % 2 == 0: continue # %연산자는 나눗셈 후 나머지를 반환한다. 즉 나머지가 0이 아니면 홀수라는 의미.
    print(a)



# while문 강제로 빠져나가기

coffee = 10
money = 300 # money가 300으로 고정되어 있음.
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


coffee = 10 # 커피의 수량은 총 10잔.
while True:
    money = int(input("돈을 넣어 주세요: ")) # 사용자로부터 값을 입력받는 부분이고 입력받은 숫자를 money 변수에 대입하는 것.
    if money == 300: # 커피 가격인 300원을 알맞게 넣었을 때 커피를 준다는 의미.
        print("커피를 줍니다.")
        coffee = coffee -1 # 하나 팔았으니까 -1.
    elif money > 300: # 만약 커피 가격보다 높은 돈을 넣었을 때, 커피 가격을 차감한 나머지를 반환함.
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1 # 역시 하나를 팔았으니 -1.
    else: # 남은 경우, 커피 가격보다 적은 금액을 넣었을 때는 도로 뱉어낸다.
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee) # 커피를 팔지 않았으므로 수량이 변하지 않음.
    if coffee == 0: # 커피를 다 팔아서 수량이 0이 되었을 때,
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.") # 다 팔렸다는 문구를 출력하고,
        break # break문을 호출하여 while문을 빠져나간다.


# while문의 맨 처음으로 돌아가기 : continue문

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


# 무한 루프

while True: # while의 조건문이 True이므로 항상 참이 된다.
    print("Ctrl + C를 눌러야 while문을 빠져나갈 수 있습니다.")













