class addn:
   def __init__(self, k, l):
        self.k = k
        self.l = l 
   def __str__(self):
       return ("("+"+"+" "+str(self.k)+" "+str(self.l)+ ")")
class mul:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def __str__(self):   
       return ("("+"*"+" "+str(self.x)+" "+str(self.y)+ ")")   
class l :
    def __init__(self,list):
        self.list = list
    def __str__(self):
        if len(self.list) == 4 and self.list[0] == 'if' :
            return ("( " + str(self.list[0]) +" " + str(self.list[1]) + " " + str(self.list[2]) + " " + str(self.list[3]) + " )")
        if len(self.list) == 1:
            return(str(self.list[0]))
        elif len(self.list) >= 2:
            return("(" + " " + str(self.list[0]) + " " +  str(self.list[1]) + " " + str(self.list[2])+ " " + ")")
def plugs(lists):
    if(lists[1] == 'l'):
        lists[1] = addn(1,1)
        return ( "( " + str(lists[0]) + " " + str(lists[1]) + " " + str(lists[2]) + " " + str(lists[3]) +" )"   )
    elif (lists[2] == 'l'):
        lists[2] = addn(1,1)
        return ( "( " + str(lists[0]) + " " + str(lists[1]) + " " + str(lists[2]) + " " + str(lists[3]) +" )"   )    
    elif (lists[3] == 'l'):
        lists[3] = addn(1,1)
        return ( "( " + str(lists[0]) + " " + str(lists[1]) + " " + str(lists[2]) + " " + str(lists[3]) +" )"   )
print(l(["if","l",2,5]))
print(plugs(["if ","l",23,15]))
print(plugs(["if ","l",3,12]))