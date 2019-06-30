class interp :
    def __init__ (self,list):
        self.list = list
    def __str__(self):
        if(self.list[4] == 'X'):
            return ( "[" +str(self.list[0]) + " " + str(self.list[1])  + " " + str(self.list[2])  + " " + str(self.list[3]) + " " + str(self.list[4]) + " ]"   )
        elif (self.list[1] == 'X' and self.list[2] == 'holes'):
            self.list[2] = "78 > 67"
            return ( "[ " + str(self.list[0]) + " " + "," + " " + str(self.list[1])  + " " + " [ if " + str(self.list[2])  + " " + str(self.list[3]) + " " + str(self.list[4]) + " ]" + " ]"  )
        elif (self.list[1] == 'X' and self.list[2] == 'holes'):
            self.list[2] = "78 > 67"
            return ( "[ " + str(self.list[0]) + " " + "," + " " + str(self.list[1])  + " " + " [ if " + str(self.list[2])  + " " + str(self.list[3]) + " " + str(self.list[4]) + " ]" + " ]"  )
    def interp(self):
        if(self.list[0] == 'if'):
            return ( "[ " + str(self.list[1]) + " " + "," + " " + str(self.list[4])  + " " + " [ if " + " holes "  + " " + str(self.list[2]) + " " + str(self.list[3]) + " ]" + " ]"  )    
        elif (self.list[0] == 'TRUE'  and self.list[2] == 'holes'):
            self.list[2] = " 2 < 5 "
            if (eval(self.list[2])):
                return("[ " + str(self.list[3]) + " , " + str(self.list[1]) + " ]" )
            else:
                return("[ " + str(self.list[4]) + " , " + str(self.list[1]) + " ]" )
        elif (self.list[0] == 'FALSE'  and self.list[2] == 'holes'):
            self.list[2] = " 5 < 2 "
            if (eval(self.list[2])):
                return("[ " + str(self.list[3]) + " , " + str(self.list[1]) + " ]" )
            else:
                return("[ " + str(self.list[4]) + " , " + str(self.list[1]) + " ]" )
print(interp(["if","46 < 5554","TRUE","FALSE","X"]).interp())
print(interp(["if","33 < 79","TRUE","FALSE","X"]))
print("\n")
print(interp(["TRUE","X","holes","TRUE","FALSE"]))
print("\n")
print(interp(["FALSE","X","holes","TRUE","FALSE"]))
print(interp(["TRUE","X","holes","TRUE","FALSE"]).interp())
print(interp(["FALSE","X","holes","TRUE","FALSE"]).interp())
