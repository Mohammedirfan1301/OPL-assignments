class k :
    def __init__(self,lists):
        self.lists = lists
    def interp(self):
        if len(self.lists) >= 4 and str(self.lists[0]) == 'if' :
            self.lists[3] = int(add(2,3).interp())
            self.lists[4] = int(mult(4,2).interp())
            if self.lists[3] > self.lists[4] :
                return (str(self.lists[3]) + " is greater than " + str(self.lists[4]))
            else :
                return (str(self.lists[4]) + " is greater than " + str(self.lists[3]))
        elif len(str(self.lists)) >= 2:
            if str(self.lists[0]) == '+':
                return (str(self.lists[1]) + str(self.lists[2]))
            elif str(self.lists[0]) == '*' :
                return (str(self.lists[1]) * str(self.lists[2]))
class num:
   def __init__(self,z):
      self.z = z
   def interp(self):
       return self.z
class F :
    def __init__(self,func):
        self.func = func
    def __str__(self):
        if len(self.func) == 1:
            return(str(self.func[0]))   
class mult:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def interp(self):
      return self.x * self.y
   def __str__(self):   
       return ("("+"*"+" "+str(self.x)+" "+str(self.y)+ ")")  
class add:
   def __init__(self, k, l):
        self.k = k
        self.l = l 
   def interp(self):
      return self.k + self.l
   def __str__(self):
       return ("("+"+"+" "+str(self.k)+" "+str(self.l)+ ")")
class V:
    def __init__(self,val):
      self.val = val
    def __str__ (self):
        if isinstance(self.val,(int,float,bool)) :
            return(str(self.val))
        if isinstance(self.val,str) :
            return(str(self.val))
class X :
    def __init__ (self,varnam):
        self.varnam = varnam
    def __str__(self):
        if len(self.var) == 1:
            return(str(self.lists[0]))
class prim:
    def __init__(self,oper):
      self.oper = oper
    def interp(self):
         if len(str(self.oper)) >= 2:
            if str(self.oper[0]) == '+':
                return (str(self.oper[1]) + str(self.oper[2]))
            elif str(self.lists[0]) == '*' :
                return (str(self.lists[1]) * str(self.lists[2]))
            elif str(self.oper[0]) == '>' :
                return (str(self.oper[2]) + "is greater than" + str(self.oper[3]))
            elif str(self.oper[0]) == '<' :
                return (str(self.oper[1]) +"is less than" + str(self.lists[2]))
            elif str(self.lists[0]) == '>=' :
                return (str(self.lists[1]) +" is greater than equal to" +str(self.lists[2]))
            elif str(self.oper[0]) == '<=' :
                return (str(self.lists[1]) +"is less than equal to" +str(self.lists[2]))
            elif str(self.oper[0]) == '=' :
                return (str(self.oper[1]) +" is equal to" +str(self.lists[2]))
    def __str__(self):
        if len(self.oper) == 1:
            return(str(self.oper[0]))
        elif len(self.oper) >= 2:
            # print(self.oper)
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
