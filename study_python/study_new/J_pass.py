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


class FlyableAttackUnit(AttackUnit, Flyable):

    def __init__(self, name , hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 건물 
class BuildingUnit(Unit):

    def __init__(self, name, hp, location):
        pass  # 일단은 완성된것처럼 넘어간다 보통은 오류걸려서 여기서 끝나야함

    
# 서플라이디폿 : 건물, 1개건물, 건물 = 8 유닛.
supply_depot = BuildingUnit("supply_depot", 500, "7시")

# 드랍십 : 공중유닛, 수송기, 마린/ 파이어뱃/ 탱크등을 수송, 공격은 불가
# 메딕 : 의무병, 공격기능없음
# 발키리 : 공중 공격유닛 , 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
# 이전과 똑같이 실행됨을 알 수 있다.

# Unit <- AttackUnit <- FlyableAttackInit -> Flyable
#  
