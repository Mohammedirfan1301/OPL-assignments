class Enum :
    def __init__(self,l):
        self.l = l
    def interpreter(self):
        if len(self.l) == 4 and self.l[0] == 'if' :
            if self.l[2] > self.l[3] :
                return (self.l[2] + "is greater than" + self.l[3])
            else :
                return (self.l[3] + "is greater than" + self.l[2])
        elif len(self.l) >= 2:
            if self.l[0] == '+':
                return (self.l[1] + self.l[2])
            elif self.l[0] == '*' :
                return (self.l[1] * self.l[2])
            elif self.l[0] == '/' :
                return (self.l[1] / self.l[2])
            elif self.l[0] == '-' :
                return (self.l[1] - self.l[2])
    def __str__(self):
        if len(self.l) == 1:
            return(str(self.l[0]))
        if len(self.l) == 4 and self.l[0] == 'if' :
            return (str(self.l[0]) +" " + "(" + " " + str(self.l[1]) + " " + ")" + " " + str(self.l[2]) + " " + str(self.l[3]))
        elif len(self.l) >= 2:
            return("(" + " " + str(self.l[0]) + " " +  str(self.l[1]) + " " + str(self.l[2])+ " " + ")")
class V:
    def __init__(self,values):
      self.values = values
    def __str__ (self):
        if isinstance(self.values,(int,float,bool)) :
            return(str(self.values))
        if isinstance(self.values,str) :
            return(str(self.values))
class prim:
    def __init__(self,o):
      self.o = o
    def interpreter(self):
         if len(self.o) >= 2:
            if self.o[0] == '+':
                return (self.o[1] + self.o[2])
            elif self.o[0] == '*' :
                return (self.o[1] * self.o[2])
            elif self.o[0] == '/' :
                return (self.o[1] / self.o[2])
            elif self.o[0] == '-' :
                return (self.o[1] - self.o[2])
            elif self.o[0] == '>' :
                return (self.o[2] + "is greater than" + self.o[3])
            elif self.o[0] == '<' :
                return (self.o[1] +"is less than" + self.o[2])
            elif self.o[0] == '>=' :
                return (self.o[1] +" is greater than equal to" +self.o[2])
            elif self.o[0] == '<=' :
                return (self.o[1] +"is less than equal to" +self.o[2])
            elif self.o[0] == '=' :
                return (self.o[1] +" is equal to" +self.o[2])
    def __str__(self):
        if len(self.o) == 1:
            return(str(self.o[0]))
        elif len(self.o) >= 2:
            string = " "
            for i in range(len(self.o)):
                string = string + str(self.o[i])
        return("(" +" " + string +" "+ ")")
print(Enum(["if",">= 11 12"," 11 ", " 12 "]))
print(Enum(["if",">= 11 12"," 11 ", " 12 "]).interpreter())
print(Enum(["*",12,12]))
print(Enum(["*",12,12]).interpreter())
print(Enum(["+",12,12]))
print(Enum(["+",12,12]).interpreter())
print(prim(["/", 69, 3] ) )
print(prim(["/", 1386, 693 ] ).interpreter() )