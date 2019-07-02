
class mul:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def __str__(self):   
       return ("("+"*"+" "+str(self.x)+" "+str(self.y)+ ")")  
class num:
   def __init__(self,z):
      self.z = z
class add:
   def __init__(self, k, e):
        self.k = k
        self.e = e 
   def __str__(self):
       return ("("+"+"+" "+str(self.k)+" "+str(self.e)+ ")")
class F :
    def __init__(self,func):
        self.func = func
    def __str__(self):
        if len(self.func) == 1:
            return(str(self.func[0]))   
print(k(["if", prim(["<"]),"5 8",add(2,3), mul(4,2)]))
class K :
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if len(self.lists) >= 4 and self.lists[0] == 'if' :
            return ("( " + str(self.lists[0]) +" " + str(self.lists[1]) + " " + str(self.lists[2]) + " " + str(self.lists[3]) + " " +  str(self.lists[4])+ " )")
        elif len(str(self.lists)) == 1:
            return(str(self.lists[0]))
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
class prim:
    def __init__(self,oper):
      self.oper = oper
    def __str__(self):
        if len(self.oper) == 1:
            return(str(self.oper[0]))
        elif len(self.oper) >= 2:
            # print(self.oper)
            string = " "
            for i in range(len(self.oper)):
                string = string + str(self.oper[i])
        return("(" +" " + string +" "+ ")")
class F :
    def __init__(self,func):
        self.func = func
    def __str__(self):
        if len(self.func) == 1:
            return(str(self.func[0]))   
print(k(["if", prim(["<"]),"5 8",add(2,3), mul(4,2)]))
class X :
    def __init__ (self,varnam):
        self.varnam = varnam
    def __str__(self):
        if len(self.var) == 1:
            return(str(self.lists[0]))
