absent = [2, 5]  # 결석
no_book = [7]
for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10 번까지인 사람을 생성
    if student in absent: #만약 결석자와 해당 번호가 같다면 그냥 지나감
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}번은 끝나고 교무실로 와!".format(student))
        break
    print("{0}번, 책을 읽어봐".format(student)) #2,5은 스킵하고 넘어감
