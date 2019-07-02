
class V:
    def __init__(self,values):
      self.values = values
    def __str__ (self):
        if isinstance(self.values,(int,float,bool)) :
            return(str(self.values))
        if isinstance(self.values,str) :
            return(str(self.values))
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
class prime:
    def __init__(self,operation):
      self.operation = operation
    def __str__(self):
        if len(self.operation) == 1:
            return(str(self.operation[0]))
        elif len(self.operation) >= 2:
            # print(self.operation)
            string = " "
            for i in range(len(self.operation)):
                string = string + str(self.operation[i])
            
        return("(" +" " + string +" "+ ")")
object = E(["if","< a b"," b is greater"," a is greater"])
class sxpr: pass
class empty(sxpr):
    def __init__(self,e_tple):
      self.e_tple = e_tple
      e_tple = ()
    def mt(self):
      return self.e_tple
class cons(sxpr) :
    def __init__(self,const):
      self.const = const
    def __str__(self):
     return (str(self.const))
class strings(sxpr):
    def __init__(self,strng1,strng2):
      self.strng1 = strng1
      self.strng2 = strng2
    def strgs(self):
      return (self.strng1)
    def __str__(self):
     return (str(self.strng1)+" " +str(self.strng2))
class pair(sxpr):
    def __init__(self,tup1):
      self.tup1 = tup1 
    def pairs(self):
      return (self.tup1)      
obj = empty(())    
obj1 = strings('if', strings("(",strings("< a b",strings(")",strings("b is greater", "a is greater")))))  
def desugarsj (obj1):
    print(object) 
desugarsj(object)
class let:
    def __init__(self,letlist):
        self.letlist = letlist
    def __str__(self):
        return("desugar of let( [" + str(self.letlist[0]) + " " + str(self.letlist[2]) + " ] [ " + str(self.letlist[1]) + " " + str(self.letlist[3]) + " ] ) is:" )
    def desugarlet(self):
        return("( \u03BB [" + str(self.letlist[0]) + " " + str(self.letlist[1]) + " ] " + str(self.letlist[2]) + " " + str(self.letlist[3]) + " )" )
print(let(["x","y",82,37]))
print(let(["x","y",82,37]).desugarlet())
