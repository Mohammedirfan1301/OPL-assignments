class E :
    def __init__(self,l):
        self.l = l
    def __str__(self):
        if len(self.l) == 1:
            return(str(self.l[0]))
        if len(self.l) == 4 and self.l[0] == 'if' :
            return (str(self.l[0]) +" " + "(" + " " + str(self.l[1]) + " " + ")" + " " + str(self.l[2]) + " " + str(self.l[3]))
        elif len(self.l) >= 2:
            return("(" + " " + str(self.l[0]) + " " +  str(self.l[1]) + " " + str(self.l[2])+ " " + ")")
class V:
    def __init__(self,values):
      self.values = values
    def __str__ (self):
        if isinstance(self.values,(int,float,bool)) :
            return(str(self.values))
        if isinstance(self.values,str) :
            return(str(self.values))
class prim:
    def __init__(self,o):
      self.o = o
    def __str__(self):
        if len(self.o) == 1:
            return(str(self.o[0]))
        elif len(self.o) >= 2:
            # print(self.o)
            string = " "
            for i in range(len(self.o)):
                string = string + str(self.o[i])
            
        return("(" +" " + string +" "+ ")")
object = E(["if","> x y"," x is greater"," y is lower "])
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
class strings(sr):
    def __init__(self,strgs1,strgs2):
      self.strgs1 = strgs1
      self.strgs2 = strgs2
    def strgs(self):
      return (self.strgs1)
    def __str__(self):
     return (str(self.strgs1)+" " +str(self.strgs2))
class pair(sr):
    def __init__(self,tup1):
      self.tup1 = tup1 
    def pairs(self):
      return (self.tup1)      
obj = (())    
obj1 = strings('if', strings("(",strings("> x y",strings(")",strings("x is greater", "a is  lower")))))  
def desugarsj (obj1):
    print(object) 
desugarsj(object)