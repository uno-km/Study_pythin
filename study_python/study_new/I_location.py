# 지역변수 : 함수내에서  , 전역번수  : 모든곳에서 가능
gun = 10

#
# def checkpoint(soldiers):
#     gun2 = 20 
#     gun2 = gun2 - soldiers
#     print("[함수 내] 남은 총 : {0}자루".format(gun2))


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}자루".format(gun))


def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}자루".format(gun))
    return gun

    
print("전체 총 : {0}".format(gun))  # 밖에있는  건을 쓴게아니다..!?
checkpoint(2) 
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))
