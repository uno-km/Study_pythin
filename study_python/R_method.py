class Unit:

    def __init__(self, name, hp, damage):  # __init__ 자동으로 호출되는 생성자
        self.name = name  # self.name  =  멤버변수다 
        self.hp = hp  # 멤버변수란 ? 클래스안에서 선언된 변수
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("hp : {0}, damage : {1}".format(self.hp, self.damage))

        
class AttackUnit:  # 공격유닛

    def __init__(self, name, hp, damage):  # __init__ 자동으로 호출되는 생성자
        self.name = name  # self.name  =  멤버변수다 
        self.hp = hp  # 멤버변수란 ? 클래스안에서 선언된 변수
        self.damage = damage
        
    def attact(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name , damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

        
# 파이어뱃 : 공격유닛, 화얌방사기    
firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attact("5시")

firebat1.damaged(25)
firebat1.damaged(25)
