class prim:
    def __init__(self,o):
      self.o = o
    def __str__(self):
        if len(self.o) == 1:
            return(str(self.o[0]))
        elif len(self.o) >= 2:
            strng = " "
            for i in range(len(self.o)):
                strng = strng + str(self.o[i])
            
        return("(" +" " + strng +" "+ ")")
class V:
    def __init__(self,value):
      self.value = value
    def __str__ (self):
        if isinstance(self.value,(int,float,bool)) :
            return(str(self.value))
        if isinstance(self.value,str) :
            return(str(self.value))
class Enum :
    def __init__(self,l):
        self.l = l
    def __str__(self):
        if len(self.l) == 1:
            return(str(self.l[0]))
        if len(self.l) == 4 and self.l[0] == 'if' :
            return (str(self.l[0]) +" " + "(" + " " + str(self.l[1]) + " " + ")" + " " + str(self.l[2]) + " " + str(self.l[3]))
        elif len(self.l) >= 2:
            return("(" + " " + str(self.l[0]) + " " +  str(self.l[1]) + " " + str(self.l[2])+ " " + ")")
print(prim(["<"]))
print(Enum([">",5,5 ]))
print(prim(["=", 6, 8 ] ) )
print(Enum(["if",">= 11 2",8,99]))