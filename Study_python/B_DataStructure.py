#자료구조의 변경
menu =  {"커피","우유","주스"}
print(menu,type(menu)) #이 자료형태가 set이란걸 알려줌 출력시 {}대괄호
menu = list(menu)
print(menu,type(menu)) #리스트로 감싸면서 리스트로형으로 바뀜 출력시 [] 중괄호
menu = tuple(menu)
print(menu,type(menu)) #튜플로 변환 출력시 () 소괄호

menu = set(menu)
print(menu,type(menu)) #다시 원상태로~ 하면 집합 형태로 바꿀수있다.'
