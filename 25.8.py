    def __init__(self, a, b, c):
               self.a=a
               self.b=b
               self.c=c
       def area(self):
               s=(self.a+self.b+self.c)/2
               area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
               return area
if __name__=='__main__':
       t1=triangle(4,13,15)
       print ('area = ',t1.area())
       