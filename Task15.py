class addn:
   def __init__(self, d, e):
        self.d = d
        self.e = e 
   def __str__(self):
       return ("("+"+"+" "+str(self.d)+" "+str(self.e)+ ")")
class mul:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def __str__(self):   
       return ("("+"*"+" "+str(self.x)+" "+str(self.y)+ ")")   
class plugs :
    def __init__ (self,temp):
        self.temp = temp
    def __str__(self):
        if(self.temp[1] == 'hole'):
            self.temp[1] = addn(1,1)
            return ( "( if  (" + str(self.temp[0]) + " " + str(self.temp[1])  +" "+ str(self.temp[2]) + " )" + " " +str(self.temp[3]) +" " + str(self.temp[4]) + " )"   )
        elif (self.temp[2] == 'hole'):
            self.temp[2] = addn(1,1)
            return ( "( if  (" + str(self.temp[0]) + " " + str(self.temp[1])  +" "+ str(self.temp[2]) + " )" + " " +str(self.temp[3]) +" " + str(self.temp[4]) + " )"   )
        elif (self.temp[3] == 'hole'):
            self.temp[3] = addn(1,1)
            return ( "( if  (" + str(self.temp[0]) + " " + str(self.temp[1])  +" "+ str(self.temp[2]) + " )" + " "+str(self.temp[3]) +" " + str(self.temp[4]) + " )"   )
    def intt(self):
        if(self.temp[1] == 'hole'):
            self.temp[1] = addn(1,1)
            if (self.temp[0] == '<'):
                return(str(self.temp[3]))
            elif (self.temp[0] == '>'):
                return(str(self.temp[4]))
        elif (self.temp[2] == 'hole'):
            self.temp[2] = addn(1,1)
            if (self.temp[0] == '<'):
                return(str(self.temp[4]))
            elif (self.temp[0] == '>'):
                return(str(self.temp[3]))
        elif (self.temp[3] == 'hole'):
            self.temp[3] = addn(1,1)
            if (self.temp[0] == '<'):
                return(str(self.temp[3]))
            elif (self.temp[0] == '>'):
                return(str(self.temp[4])) 
print(plugs(["<","hole",'a',"5 is greater","b is lower"]))
print(plugs(["<","hole",35,"5 is greater","6 is greater"]).intt())
print(plugs([">",16,"hole",2,8]))
print(plugs([">",15,"hole",13,14]).intt())