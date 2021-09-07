class Unit:  # 일반 유닛(공격기능이 없음) #이걸 부모클래스라고함

    def __init__(self):  # __init__ 자동으로 호출되는 생성자
        print("Unit 생성자")


# 다중상속은 자식이 다수의 부모를 상속받는것이다.
class Flyable:  # 날수 있는 기능을 가진 클래스
    
    def __init__(self):
        print("Flyable 생성자")

    
class FlyableUnit(Flyable, Unit):
# class FlyableUnit(Unit, Flyable):

    def __init__(self):
       # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍십
dropship = FlyableUnit()
