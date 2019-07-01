class interp :
    def __init__ (self,lists):
        self.lists = lists
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
    def interp(self):
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
print(interp(["kif","1","<","27","K0"]))
print(interp(["kif","22","<","23","K0"]).interp())
print("\n")
print(interp([">","kapp",51,452,"Kif" , "K0"]))
print(interp(["if","27 < 123","TRUE then 27","FALSE then 123","K0"]))
print(interp(["if","27 < 123","TRUE then 27","FALSE then 123","K0"]).interp())
print("\n")
print(interp(["TRUE","K","SATISFIED","NOT-SATISFIED","K"]))
print(interp(["TRUE","K","SATISFIED","NOT-SATISFIED","K"]).interp())
print("\n")
print(interp(["FALSE","K","SATISFIED","NOT-SATISFIED","K"]))
print(interp(["FALSE","K","SATISFIED","NOT-SATISFIED","K"]).interp())
print("\n")
print(interp([">","kapp",5123,223,"Kif" , "K0"]).interp())
