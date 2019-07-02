class addn:
   def __init__(self, k, l):
        self.k = k
        self.l = l 
   def interp(self):
      return self.k + self.l
   def __str__(self):
       return ("("+"+"+" "+str(self.k)+" "+str(self.l)+ ")")  
class number:
   def __init__(self,z):
      self.z = z
   def interp(self):
       return self.z
class l :
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if len(self.lists) == 1:
            return(str(self.lists[0]))
        if len(self.lists) == 4 and self.lists[0] == 'if' :
            return (str(self.lists[0]) +" " + "(" + " " + str(self.lists[1]) + " " + ")" + " " + str(self.lists[2]) + " " + str(self.lists[3]))
        elif len(self.lists) >= 2:
            return("(" + " " + str(self.lists[0]) + " " +  str(self.lists[1]) + " " + str(self.lists[2])+ " " + ")")
class mul:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def interp(self):
      return self.x * self.y
   def __str__(self):   
       return ("("+"*"+" "+str(self.x)+" "+str(self.y)+ ")")  
class V:
    def __init__(self,val):
      self.val = val
    def __str__ (self):
        if isinstance(self.val,(int,float,bool)) :
            return(str(self.val))
        if isinstance(self.val,str) :
            return(str(self.val))
class prim:
    def __init__(self,oper):
      self.oper = oper
    def __str__(self):
        if len(self.oper) == 1:
            return(str(self.oper[0]))
        elif len(self.oper) >= 2:
            string = " "
            for i in range(len(self.oper)):
                string = string + str(self.oper[i])
            
        return("(" +" " + string +" "+ ")")
class X :
    def __init__ (self,varnam):
        self.varnam = varnam
    def __str__(self):
        return(str(self.varnam[0]))
print(l(["if","< 12 57",12,57]))
print(l(["<",3,4 ]))
print(prim([">="]))
print(prim(["/"]))
print(V(7))
print(X(["variable"]))
print(l(["irfan"]))
print(V(7.5))
print(V(True))
print(l(["if","> 12355","true","false"]))
print(prim(["<"]))
print(prim([">=", 1211, 212 ] ) )