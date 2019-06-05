class sr: pass
class full(sr):
    def __init__(self,full_order):
      self.full_order = full_order
      full_order = ()
    def mt(self):
      return self.full_order
class cons(sr) :
    def __init__(self,cst):
      self.cst = cst
    def __str__(self):
     return (str(self.cst))
class strngs(sr):
    def __init__(self,strg1,strg2):
      self.strg1 = strg1
      self.strg2 = strg2
    def strgs(self):
      return (self.strg1)
    def __str__(self):
     return (str(self.strg1)+" " +str(self.strg2))
class pairing(sr):
    def __init__(self,tup1):
      self.tup1 = tup1 
    def pairings(self):
      return (self.tup1)      
obj = full(())    
obj1 = strngs('(', strngs("*",strngs(cons(3),strngs("(",strngs("+", strngs(cons(5),strngs(cons(3),") )")))))))  

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
obje = addn(3,mul(5,3)) 
def dssj (obj1):
    print(obje) 
dssj(obje)