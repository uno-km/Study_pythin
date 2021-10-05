# 마린  : 공격 유닛, 군인. 총을 쏠 수 있음
name = "marin"  # 유닛의 이름
hp = 40
damage = 5
print("{0} 유닛이 생성되었습니다. ".format(name))
print("hp : {0}, damage : {1}\n".format(hp, damage))

# tank : attacker, tank, nomal mode, size mode
tank_name = "tank"
tank_hp = 150
tank_damage = "35"
tank_name2 = "tank"
tank_hp2 = 150
tank_damage2 = "35"
print("{0} 유닛이 생성되었습니다. ".format(tank_name))
print("hp : {0}, damage : {1}\n".format(tank_hp, tank_damage))


def attack(name , lacation, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
            name, lacation, damage))

    
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank_name2, "1시", tank_damage2)

# 계속 탱크를 늘려갈순있지만, 무한정만들기엔 어렵다. 따라서 클래스를 만들어 관리한다면 좀더 편하다
print("--- class를 이용---")


class Unit:

    def __init__(self, name, hp, damage):  # __init__ 자동으로 호출되는 생성자
        self.name = name  # self.name  =  멤버변수다 
        self.hp = hp  # 멤버변수란 ? 클래스안에서 선언된 변수
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("hp : {0}, damage : {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)  # 뒤에는 인스턴스이다, 셀프를 제외하고 동일한 개수의 값을 던져주어야한다.
marine2 = Unit("마린", 40, 5)  # 만약 이름정보만, 또는 이름과 체력정보만 보내주면 오류가뜸!! 따라서 곧뒤져도 인스턴스개수를 맞춰줘야함! ㅎ
tank = Unit("탱크", 150, 35)

# 레이스 유닛, 특수한 기능도있음 (클록킹 : 상대방에게 보이지않음)
wraith1 = Unit("레이스", 80, 5)
print("unit name : {0}, damage : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 기술을 넣음
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} is clocking now".format(wraith2.name))
    # 레이스 1에는 클록킹이없다 !
