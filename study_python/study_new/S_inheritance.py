class Unit:  # 일반 유닛(공격기능이 없음) #이걸 부모클래스라고함

    def __init__(self, name, hp):  # __init__ 자동으로 호출되는 생성자
        self.name = name  # self.name  =  멤버변수다 
        self.hp = hp  # 멤버변수란 ? 클래스안에서 선언된 변수

        
class AttackUnit(Unit):  # 공격유닛 #자식클래스

    def __init__(self, name, hp, damage):  # __init__ 자동으로 호출되는 생성자
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attact(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name , damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

        
# 메딕 : 의무병, 공격기능없음
firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attact("5시")

firebat1.damaged(25)
firebat1.damaged(25)
# 이전과 똑같이 실행됨을 알 수 있다.
