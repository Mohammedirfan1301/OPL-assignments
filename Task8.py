class prime:
    def __init__(self,o):
      self.o = o
    def __str__(self):
        if len(self.o) == 1:
            return(str(self.o[0]))
        elif len(self.o) >= 2:
            string = " "
            for i in range(len(self.o)):
                string = string + str(self.o[i])
            
        return("(" +" " + string +" "+ ")")
class v:
    def __init__(self,value):
      self.value = value
    def __str__ (self):
        if isinstance(self.value,(int,float,bool)) :
            return(str(self.value))
        if isinstance(self.value,str) :
            return(str(self.value))
class e :
    def __init__(self,list):
        self.list = list
    def __str__(self):
        if len(self.list) == 1:
            return(str(self.list[0]))
        if len(self.list) == 4 and self.list[0] == 'if' :
            return (str(self.list[0]) +" " + "(" + " " + str(self.list[1]) + " " + ")" + " " + str(self.list[2]) + " " + str(self.list[3]))
        elif len(self.list) >= 2:
            return("(" + " " + str(self.list[0]) + " " +  str(self.list[1]) + " " + str(self.list[2])+ " " + ")")
print(e(["perk"]))
print(e(["if","< 11 9",8,5]))
print(e(["<",6,9 ]))
print(prime([">="]))
print(prime(["<=", 4, 5 ] ) )
