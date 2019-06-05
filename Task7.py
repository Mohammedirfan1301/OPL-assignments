class sr: pass
class empty(sr):
    def __init__(self,order):
      self.order = order
      order = ()
    def mt(self):
      return self.order
class cons(sr) :
    def __init__(self,cst):
      self.cst = cst
    def __str__(self):
     return (str(self.cst))
class strng(sr):
    def __init__(self,strng1,strng2):
      self.strng1 = strng1
      self.strng2 = strng2
    def strgs(self):
      return (self.strng1)
    def __str__(self):
     return (str(self.strng1)+" " +str(self.strng2))
class pairing(sr):
    def __init__(self,tup1):
      self.tup1 = tup1 
    def pairings(self):
      return (self.tup1)      
obj = empty(())    
obj1 = strng('(', strng("*",strng(cons(3),strng("(",strng("+", strng(cons(5),strng(cons(3),") )"))))))) 
class ds: pass
class mul(ds):
   def __init__(self, d, e):
      self.d = d
      self.e = e
   def __str__(self):   
       return ("("+"*"+" "+str(self.d)+" "+str(self.e)+ ")")   
class addn(ds):
   def __init__(self, x, y):
        self.x = x
        self.y = y 
   def __str__(self):
       return ("("+"+"+" "+str(self.x)+" "+str(self.y)+ ")")    
object = addn(8,mul(7,5)) 
def dssf (obj1):
    print(object) 
dssf(object)