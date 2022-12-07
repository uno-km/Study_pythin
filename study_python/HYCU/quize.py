class Lecture:
    def __init__(self,name ='Python'):
        self.lectname  =name
    def prn_lectname(self):
        print(f'your lecture name is {self.lectname}')
        
class Mylecture(Lecture):
    def prn_lectname(self):
        print(f'my lectuyre name is {self.lectname}')

mylectname =  Mylecture('Com')
mylectname.prn_lectname()