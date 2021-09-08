# 다중상속은 자식이 다수의 부모를 상속받는것이다.
from jedi.debug import speed
from debugpy._vendored.pydevd.pydevd_attach_to_process.winappdbg.win32.defines import TRUE, \
    FALSE


class Flyable:  # 날수 있는 기능을 가진 클래스
    
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(self.name, location, self.flying_speed))


class Unit:  # 일반 유닛(공격기능이 없음) #이걸 부모클래스라고함

    def __init__(self, name, hp, speed):  # __init__ 자동으로 호출되는 생성자
        self.name = name  # self.name  =  멤버변수다 
        self.hp = hp  # 멤버변수란 ? 클래스안에서 선언된 변수
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        print("[지상유닛이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}".format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name , damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

        
class AttackUnit(Unit):  # 공격유닛 #자식클래스

    def __init__(self, name, hp, damage):  # __init__ 자동으로 호출되는 생성자
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attact(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))


# 마린 클래스
class Marine(AttackUnit):

    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 6)
        
    # 스팀팩 : 일정시간 동안 이동 및 공격속도를 증가, 자기 체력 10감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
    

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격가능, 이동불가
    seize_developed = False
    
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 40, 1, 35)
        self.seize_mode = False
        
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if Tank.seize_developed == True:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일때 -> 일반모드
        else:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

        
class FlyableAttackUnit(AttackUnit, Flyable):

    def __init__(self, name , hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


class Wraith(FlyableAttackUnit):

    def __init__(self):
        FlyableAttackUnit.__init__("레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드 (해제상태)
        
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹모드를 설정합니다.".format(self.name))
            self.clocked = True


# 드랍십 : 공중유닛, 수송기, 마린/ 파이어뱃/ 탱크등을 수송, 공격은 불가
# 메딕 : 의무병, 공격기능없음
# 발키리 : 공중 공격유닛 , 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
# 이전과 똑같이 실행됨을 알 수 있다.

# Unit <- AttackUnit <- FlyableAttackInit -> Flyable
#  
