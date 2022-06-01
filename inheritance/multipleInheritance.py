
# media resolution order according to this. 
# accoding to mro first activated class is C, then B and lastly C
class A:
    def __init__(self):
        super().__init__()
        self.foo = 'foo'
        self.name = 'this is A'


class B:
    def __init__(self):
        super().__init__()
        self.bar = 'bar'
        self.name = 'this is B'


class C(B, A):
    def __init__(self):
        super().__init__()
        self.name = 'this is c'
    
    def showProps(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

c = C()
c.showProps()

    