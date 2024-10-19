import random

lotto_num = []  # 빈 리스트를 생성하여 로또 번호를 저장할 준비를 한다.

def getRandowNumber():  # 랜덤한 숫자를 반환하는 함수를 정의한다.
    number = random.randint(1, 45)  # 1부터 45 사이의 랜덤한 숫자를 생성한다.
    return number

count = 0  # 카운트 변수를 초기화한다.

while True:  # 무한 루프를 시작한다.
    if count > 5:  # 만약 카운트가 6이면
        break  # 루프를 빠져나간다.

    random_number = getRandowNumber()  # 랜덤한 숫자를 생성한다.

    if random_number not in lotto_num:  # 만약 생성한 숫자가 lotto_num 리스트에 없으면
        lotto_num.append(random_number)  # lotto_num 리스트에 추가한다.
        count = count + 1  # 카운트를 1 증가시킨다.

print(lotto_num)  # lotto_num 리스트를 출력한다.