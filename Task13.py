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
class V :
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if self.lists[1] == 'y':
            return(" the context format is variant-1")
        elif self.lists[2] == 'y':
            return(" the context format is variant-2")
        elif self.lists[3] == 'y':
            return(" the context format is variant-3")
def plug(temp_list):
    if(temp_list[1] == 'PLUG'):
        temp_list[1] = mul(1,1)
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
    elif (temp_list[2] == 'PLUG'):
        temp_list[2] = mul(7,addn(1,1))
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
    elif (temp_list[3] == 'PLUG'):
        temp_list[3] = addn(8,12)
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
print(plug(["< ","PLUG",12,13,14]))
print(plug(["< ",0,"PLUG",0,0]))
print(plug(["< ",20,"PLUG",12,98]))