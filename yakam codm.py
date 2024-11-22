
class hasiba:
    def __init__(self,num1=0,num2=0):
        self.num1=int(input('zhmaray yakam daxlbka ; '))
        self.num2=int(input('zhmaray dwam daxlbka; '))
        self.run()
    def run(self):
        print('+,-,*,/')
        s =input('diarybka chyt dawe; ')
        while True:
          if s =='+':
              self.ko()
              break

          elif s =='_':
              self.kam()
              break
          elif s=='*':
              self.jaran()
              break
          elif s =='/':
              self.dabash()
              break
          else:
              print('xalata')
              break
    def ko(self):
        r =self.num1+ self.num2
        print(r)

    def kam (self):
        r= self.num1-self.num2
        print(r)
    def dabash(self):
        r= self.num1/self.num2
        print(r)
    def jaran (self):
        r= self.num1*self.num2
        print(r)
x=hasiba()









