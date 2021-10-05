print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")
# 위와 같은 작업을 무한정할순 없으니 반복문을 사용해야한다.

for waiting_no in range(1, 7):
    print("waiting no. : {0}".format(waiting_no))
    
# test = range(0, 20)
# for test in:
#    print("test : {0}".format(test))

starbucks = ["아이언맨", "토르", "아이엠 구르트"]
for customer in starbucks:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
