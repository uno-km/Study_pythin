# 표준 입출력
# print("python", "java")
# print("python" + "java")
# print("python" , "java" , sep=", ")  # sep = " " 이걸 넣어주면 콤마때마다 해당 패턴을 넣어준다
# print("python", "java" , sep=", ", end = "을 배우나요? ") #이럼 end뒤는 맨뒤에 나오게됨

#end 의 의미는 마지막 부분에 어떤 단어를 ㄹ넣던가, 기본값은 엔터임
# import sys
# print("Python", "java", file=sys.stdout) #표준출력으로 찍힘
# print("Python", "java", file=sys.stderr) #표준 에러로 찍힘

#왼쪽정렬 오른쪽정렬
#시험 성적
# scores = {"math":0,"english":50,"coding":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(3), sep=" : ")
#은행 대기 순번표
#반복문에 넣기
for num in range(1,21):
    print("wating num", str(num).zfill(3), sep=" : ") #.zfill = 값이 부족한 값엔 0일 넣는다
    
    
#사용자 입력기본폼 : input을 넣는다 - 항상 문자열로 받는다
answer = input("아무 값이나 입력하세요 : " )
print("입력하신 값은 " + answer + "입니다.")
# print("입력하신 값은 " + type(answer) + "형태 입니다.")
print(type(answer))
    