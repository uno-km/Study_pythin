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


def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}" \
          .format(name, age, main_lang))

    
profile("kim", 20, "python")
profile("hwang", 25, "java")


# 같은 학교 같은 학년 같은 반 같은 수업(이름만 다름)-> 불필요한 입력폼들을 기본값으로 
def profile2(name, age=17, main_lang="java"):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}" \
          .format(name, age, main_lang))

    
profile2("kim", 20, "python")
profile2("hwang", 25)
profile2("hwang")
profile2("hwang", 15)


def profile6(name, age, lang):
    print(name, age, lang)

    
profile6(name="kim", age=20, lang="java")
profile6(name="hwang", lang="python", age="19")


def profile3(name , age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t 나이 : {1}\t ".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profile3("김은호", 20, "python", "java", "JS", "C", "C++")
profile3("천영환", 23, "Korlin", "Swift", "", "", "")


# 이때 계속 바뀌게 될 수 있다 -> 가변인수
def profile5(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile5("김은호", 20, "java", "Swift", "JS", "C", "C++", "C#")
profile5("천영환", 23, "Korlin", "Swift")
