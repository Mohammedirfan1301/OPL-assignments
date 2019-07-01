class num:
   def __init__(self,a):
      self.a = a
   def interp(self):
       return self.a
class addn:
   def __init__(self, d, e):
        self.d = d
        self.e = e 
   def interp(self):
      return self.d + self.e
   def __str__(self):
       return ("("+"+"+" "+str(self.d)+" "+str(self.e)+ ")")
class mul:
   def __init__(self, b, c):
      self.b = b
      self.c = c
   def interp(self):
      return self.b * self.c
   def __str__(self):   
       return ("("+"*"+" "+str(self.b)+" "+str(self.c)+ ")")  
class E :
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if len(self.lists) == 1:
            return(str(self.lists[0]))
        if len(self.lists) == 4 and self.lists[0] == 'if' :
            return (str(self.lists[0]) +" " + "(" + " " + str(self.lists[1]) + " " + ")" + " " + str(self.lists[2]) + " " + str(self.lists[3]))
        elif len(self.lists) >= 2:
            return("(" + " " + str(self.lists[0]) + " " +  str(self.lists[1]) + " " + str(self.lists[2])+ " " + ")")
class V:
    def __init__(self,val):
      self.val = val
    def __str__ (self):
        if isinstance(self.val,(int,float,bool)) :
            return(str(self.val))
        if isinstance(self.val,str) :
            return(str(self.val))
class prime:
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
        if len(self.var) == 1:
            return(str(self.lists[0]))
class F :
    def __init__(self,func):
        self.func = func
    def __str__(self):
        if len(self.func) == 1:
            return(str(self.func[0]))   
class D :
    def __init(self,defi1,defi2):
        self.defi1 = defi1
        self.defi2 = defi2
    def __str__(self):
        return ( str(self.defi1) + str(self.defi2) )
temp1 = addn(1,1).interp()
temp2 = mul(2,1).interp()
print( D([ E(["if"]) , E([addn(1,1) , '<' , E([addn(2,3) , temp1 , temp2 ]) ])  ]) )
print(E(["if","< 42 0",32,41]))
print(E(["<",23,17 ]))
