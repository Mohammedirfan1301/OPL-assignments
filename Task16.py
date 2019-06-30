class forms :
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if self.lists[0] == 'HOLE' :
            return("its a hole")
        if self.lists[1] == 'E':
            return(" the  format is type 1")
class hole :
    def __init__ (self,l):
        self.l = l
    def __str__(self):
        if(self.l[1] == 'E'):
            self.l[1] = '22< 19'
            return ("(" + str(self.l[0]) + " " + "(" + " " +str(self.l[1])  + " " + ")" + " " +str(self.l[2]) + " " + str(self.l[3]) +" " + ")")
    def ltrp(self):
        if(self.l[1] == 'F'):
            self.l[1] = '22  > 19'
            if (eval(self.l[1])):
                return(str(self.l[2]))
            else :
                return(str(self.l[3]))
print(hole(["if","E","True","False"]))
print(hole(["if","E","TRUE","FALSE"]).ltrp())