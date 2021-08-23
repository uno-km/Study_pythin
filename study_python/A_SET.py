
#집합
my_set = {1,2,3,4,3,3 }
print(my_set) #중복은안됨
java = {"유재석","김태호", "양세형"}
python  = set(["유재석","박명수"])

#교집합 출력(java와 python모두 할 수 있는 개발자)
print(java & python) #서로 다른집합중 교집합을 출력한다.
print(java.intersection(python)) 

#합집합 (java도 할수있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자    )
print(java - python)
print(java.difference(python))

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java 를 까먹었다
java.remove("김태호")
print(java)