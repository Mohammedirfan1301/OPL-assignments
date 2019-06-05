class Task6: pass
class blank(Task6):
    def __init__(self,order):
      self.order = order
      order = ()
    def mt(self):
      return self.order
class cons(Task6) :
    def __init__(self,cst):
      self.cst = cst
    def __str__(self):
     return (str(self.cst))
class string(Task6):
    def __init__(self,string1):
      self.string1 = string1
    def strgs(self):
      return (self.string1)
    def __str__(self):
     return ("("+str(self.string1))
class paired(Task6):
    def __init__(self,tuples):
      self.tuples = tuples 
    def pairs(self):
      return (self.tuples)      
sxpr = blank(())
print(str(string('*'))+" "+str(cons(3))+" "+str(string('+'))+" "+str(cons(5))+" "+ str(sxpr.order)+ ") )")