class Reversetler:
    def __init__(self,p):
        self.p=p
    def rev(self):
        for i in range(1,len(self.p)+1):
            print(self.p[-i],end=' ')
d=Reversetler([1,2,3,45])
d.rev()