class addn:
   def __init__(self, k, l):
        self.k = k
        self.l = l 
   def itrp(self):
      return self.k + self.l
   def __str__(self):
       return ("("+"+"+" "+str(self.k)+" "+str(self.l)+ ")") 
class mul:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def itrp(self):
      return self.x * self.y
   def __str__(self):   
       return ("("+"*"+" "+str(self.x)+" "+str(self.y)+ ")") 

class rdx:
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if(str(self.lists[0]) == str(addn(1,1))):
            self.lists[0] = "l"
            return ( "( if  (" + " " +str(self.lists[0]) + " )" + " " +str(self.lists[3]) +" " + str(self.lists[4]) + " )"   )
    def itrp(self):
        if(self.lists[0] == 'l'):
            self.lists[0] = addn(1,1)
            print ( "l X " + "( if  (" + " " + str(self.lists[0]) + " " + str(self.lists[1]) + " " + str(self.lists[2]) + " " + " )" + " " +str(self.lists[3]) +" " + str(self.lists[4]) + " )"   )
        if(str(self.lists[0]) == str(mul(33,33))):    
            self.lists[0] = addn(1,1).itrp()
            print ( "l X " + "( if  (" + " " + str(self.lists[0]) + " " + str(self.lists[1]) + " " + str(self.lists[2]) + " " + " )" + " " +str(self.lists[3]) +" " + str(self.lists[4]) + " )"   )
            if (self.lists[0] < self.lists[2] ):
                print(str(self.lists[3]))
            elif (self.lists[1] > self.lists[2] ):
                print(str(self.lists[4]))
                t =rdx([addn(33,33),"<",230,"TRUE","FALSE"])  
                print(t)
                t.itrp()
