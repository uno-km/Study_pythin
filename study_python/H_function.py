def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account() 


# 전달값과 반환값
def deposit(balance, money):
    print("입금이 완료되었음. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money


# 출금
def withdraw(balance, money):
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었음. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금 실패. 잔액은 {0} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission , balance - money - commission


balance = 1000
balance = deposit(balance , 1000)
print(balance)
balance = withdraw(balance , 500)
print(balance)
commission, balance = withdraw_night(balance , 500)
print("수수료는 {0}원이며, 잔액은 {1} 원입니다.".format(commission, balance))

