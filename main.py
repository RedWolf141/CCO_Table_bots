
import random
from dora import makeBag
from medTech import change_ts
"""
ts = tech scrp (공학 조각)
mts = medical tech scrap(의학 공학 조각)
old = 낡은 주머니
pan = panny pack (보조 가방)
dora = 모험가의 가방 (도라)


"""


ts = 0
mts = 0
while (True):
   
    print("원하시는 컨텐츠를 선택해주세요 ")
    print("1. 공조 수량 설정 \n")
    print("2. 의공조 수량 설정 \n")
    print("3. 현재 공조 개수 확인 \n")
    print("4. 현재 의공조 개수 확인 \n")
    print("5. 의공조 - 공조 변환 \n")
    print("6. 만들수 있는 가방 수량 확인. \n")
    print("7. 프로그램을 종료합니다 \n")

    number = int(input(">입력후 엔터"))

    #if (number > 5 or number < 0):
    #    number = int(input("없는 번호 입니다 다시 입력해주세요"))


    #공조값 설정
    if number == 1:
        ts = int(input("설정할 공조의 값을 정해주세요. 이미 설정된 값이 있다면 덮어 씌워집니다."))
        if (ts < 0):
            ts = print("0보다 커야 합니다. 다시 입력해주세요")
        input("엔터를 눌러서 다시 메뉴로 돌아갑니다 \n \n \n")
        

    #의공조값 설정
    elif number == 2:
        mts = int(input("설정할 의공조의 값을 정해주세요. 이미 설정된 값이 있다면 덮어 씌워집니다"))
        input("엔터를 눌러서 다시 메뉴로 돌아갑니다 \n \n \n")

        
    #공조 수량 확인
    elif number == 3:
        string = f"현재 공학 조각 수는 {ts}입니다"
        print(string)
        input("엔터를 눌러서 다시 메뉴로 돌아갑니다 \n \n \n")
    
    #의공조 수량 확인
    elif number == 4:
        string = f"현재 의공조 조각 수는 {mts}입니다"
        print(string)
        input("엔터를 눌러서 다시 메뉴로 돌아갑니다 \n \n \n")
    
    #공조 의공조 변환
    elif number == 5:
        ts = change_ts(mts)
        string = f"변환된 현재 공조 조각수는 {ts} 입니다"
        print(string)
        input("엔터를 눌러서 다시 메뉴로 돌아갑니다 \n \n \n")


    elif number == 6:
        makeBag(ts)
        input("엔터를 눌러서 다시 메뉴로 돌아갑니다 \n \n \n")

    elif number == 7:
        break
    