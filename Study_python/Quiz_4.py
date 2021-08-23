
# 퀴즈 
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 징행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됩니다.
#
# 조건1 : 편의상 댓글을 20명이 작성 아이디는 1~20개로 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용
from random import *
print("-- 당첨자 발표 --")
users = range(1, 21)  # 1~20까지 숫자생성
# print(type(users))
users = list(users)
# print(type(users))

# print(users)
shuffle(users)

winners = sample(users, 4)  # 4명중 한명은 치킨, 3명은 커피
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다. --")
