# 다중상속은 자식이 다수의 부모를 상속받는것이다.
class Flyable:  # 날수 있는 기능을 가진 클래스
    
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(self.name, location, self.flying_speed))


class Unit:  # 일반 유닛(공격기능이 없음) #이걸 부모클래스라고함

    def __init__(self, name, hp):  # __init__ 자동으로 호출되는 생성자
        self.name = name  # self.name  =  멤버변수다 
        self.hp = hp  # 멤버변수란 ? 클래스안에서 선언된 변수

        
class AttackUnit(Unit):  # 공격유닛 #자식클래스

    def __init__(self, name, hp, damage, speed):  # __init__ 자동으로 호출되는 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attact(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name , damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class FlyableAttackUnit(AttackUnit, Flyable):

    def __init__(self, name , hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 건물 
class BuildingUnit(Unit):

    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)  # 일단은 완성된것처럼 넘어간다 보통은 오류걸려서 여기서 끝나야함
        super().__init__(name, hp, 0)
        self.location = location
    
# 서플라이디폿 : 건물, 1개건물, 건물 = 8 유닛.
