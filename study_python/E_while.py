# while
customer = "tor"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다, 기회는 {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("삐빅 - 커피는 폐기처분되었습니다.")
    else:
        print("빨리오세요!")

# 조건이 맞을때 
customer = "ironman"
person = "unknown"
index = 1;
while person != customer:
    print("{0}님, 커피가 준비 되었습니다 ".format(customer))
    person = input("이름이 어떻게 되세용?")

customer = "ironman"
flag = True
while flag:
    person = input("이름이 어떻게 되세용?")
    if person == customer:
        print("주문하신 음료나왔습니다.")
        flag = False
    else:
        print("잠시만 기다려주세용")
