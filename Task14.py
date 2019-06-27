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
def redx(temp_list):
    if(str(temp_list[1]) == str(addn(1,1))):
        temp_list[1] = "PLUG"
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
    elif (str(temp_list[2]) == str(addn(1,1))):
        temp_list[2] = "PLUG"
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
    elif (str(temp_list[3]) == str(addn(1,1))):
        temp_list[3] = "PLUG"
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
print(redx(["< ",mul(1,1),15,32,14]))
print(addn(1,1))
print(redx(["< ",45,addn(5,5),8,12]))
print(mul(21,31))