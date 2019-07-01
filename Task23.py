class interp :
    def __init__ (self,lists):
        self.lists = lists
    def itrp(self):
        if(self.lists[0] == 'if'):
            return ( "[ " +str(self.lists[1]) + " " + "," + " " + "K "  + "if (" + " " + str(self.lists[2]) + " " + str(self.lists[3]) + " " + str(self.lists[4]) +" )" + " ]"  )    
        elif (self.lists[0] == 'TRUE'):
            return("[ " + str(self.lists[2]) + " , " + str(self.lists[1]) + " ]" )
        elif (self.lists[0] == 'FALSE'):
            return("[ " + str(self.lists[3]) + " , " + str(self.lists[1]) + " ]" )    
        elif (self.lists[0] == 'kif'):
            return ( "[ " +str(self.lists[2]) + " " + ", kapp ( () , ( " +str(self.lists[1])  + " " + str(self.lists[3]) + ") ,"  + " " + str(self.lists[0]) + " (" + str(self.lists[1]) + "," + str(self.lists[3]) + "," +str(self.lists[4]) + " ) ) ]"   )    
        elif (self.lists[0] == '<' and (self.lists[2] < self.lists[3]) ):
            return ( "[" +str(self.lists[3]) + " , " + str(self.lists[1])  + " (( " + str(self.lists[0]) + str(self.lists[2]) + " , ( )" + " , " + str(self.lists[4])  + "( " + str(self.lists[2]) + " , "+ str(self.lists[3]) + " , "  + str(self.lists[5]) +" ) ) ]"   )    
        elif (self.lists[0] == '>' and (self.lists[2] > self.lists[3]) ):
            return ( "[" +str(self.lists[2]) + " , " + str(self.lists[1])  + " (( " + str(self.lists[0]) + str(self.lists[3]) + " , ( )" + " , " + str(self.lists[4])  + "( " + str(self.lists[2]) + " , "+ str(self.lists[3]) + " , "  + str(self.lists[5]) +" ) ) ]"   )    
    def __str__(self):
        if (self.lists[0] == 'TRUE' ):
            return ( "[ " + str(self.lists[0]) + " " + "," + " " + str(self.lists[1])  + " " + " if [ " + str(self.lists[2])  + " " + str(self.lists[3]) + " " + str(self.lists[4]) + " ]" + " ]"  )
        if (self.lists[0] == 'FALSE'):
            return ( "[ " + str(self.lists[0]) + " " + "," + " " + str(self.lists[1])  + " " + " if [" + str(self.lists[2])  + " " + str(self.lists[3]) + " " + str(self.lists[4]) + " ]" + " ]"  )
        if(self.lists[4] == 'K0'):
            return ( "[" +str(self.lists[0]) + " " + str(self.lists[1])  + " " + str(self.lists[2])  + " " + str(self.lists[3]) + " " + str(self.lists[4]) + " ]"   )
        if(self.lists[0] == 'kif'):
            return ( "[" +str(self.lists[0]) + " " +str(self.lists[1])  + " " + str(self.lists[2]) + " " + str(self.lists[3]) + " " + str(self.lists[4])  + " ]"   )    
        if(self.lists[0] == '<' or self.lists[0] == '>'):
            return ( "[" +str(self.lists[2]) + " , " + str(self.lists[1])  + " (( " + str(self.lists[0]) + " ) , ( " + str(self.lists[3]) + " ) ," + str(self.lists[4])  + "( " + str(self.lists[2]) + " , "+ str(self.lists[3]) + " , "  + str(self.lists[5]) +" ) ) ]"   )    
    
print(interp(["if","12 < 35","TRUE then 12","FALSE then 35","K0"]))
print(interp(["if","2 < 5","TRUE then 12","FALSE then 35","K0"]).itrp())
print("\n")
print(interp(["TRUE","K","SATISFIED","NOT-SATISFIED","K"]))
print(interp(["TRUE","K","SATISFIED","NOT-SATISFIED","K"]).itrp())
print("\n")
print(interp(["FALSE","K","SATISFIED","NOT-SATISFIED","K"]))
print(interp(["FALSE","K","SATISFIED","NOT-SATISFIED","K"]).itrp())
print("\n")
print(interp(["kif","2","<","5","K0"]))
print(interp(["kif","2","<","5","K0"]).itrp())
print("\n")
print(interp(["<","kapp",2,5,"Kif" , "K0"]))
print(interp(["<","kapp",2,5,"Kif" , "K0"]).itrp())
print("\n")
