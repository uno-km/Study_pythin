# 출석번호가 1 2 3 4 가있는데, 앞에 100을 붙이기로 함. 즉 101, 102, 103, 104 가됨
student = [1, 2, 3, 4, 5]
print(student)
student = [i + 100 for i in student]
print(student)
student = [i - 100 for i in student]
print(student)

# 만약 학생 이름을 길이로 변환
students = ["kimeunoho", "kimdohwan", "chunyounghwan", "chosunginn", "hwanghunha"]
students = [len(i) for i in students]
print(students)

# 학생이름을 대문자로 변환
students = ["kimeunoho", "kimdohwan", "chunyounghwan", "chosunginn", "hwanghunha"]
students = [i.upper() for i in students]
print(students)
