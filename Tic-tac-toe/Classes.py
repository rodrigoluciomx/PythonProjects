class Player:  
    def __init__(self,input_name = None) -> None:
        self.name = input_name
        self.id = 1

    @property
    def Name(self):
        return self.name
    
    @property
    def Id(self):
        return self.id

    def actualizarID(self):
        self.id += 1

    def makeTurn(self):
        box = int(input("Select the box you want: "))
        return box - 1 
    

class Board:

    def __init__(self) -> None:
        self.template = ["_1_","_2_","_3_","_4_","_5_","_6_"," 7 "," 8 "," 9 "]

    @property
    def Template(self):
        return self.template
    
    def updateTemplate(self,box,symbol):
        self.template[box] = symbol

    def makeBoard(self):

        r_1 = self.template[0] + "|" + self.template[1] + "|" + self.template[2]
        r_2 = self.template[3] + "|" + self.template[4] + "|" + self.template[5]
        r_3 = self.template[6] + "|" + self.template[7] + "|" + self.template[8] 
    
        return r_1,r_2,r_3

    def possibleWin(self):
        if self.template[0] == self.template[1] and self.template[0] == self.template[2]:
            return True
        elif self.template[0] == self.template[3] and self.template[0] == self.template[6]:
            return True
        elif self.template[0] == self.template[4] and self.template[0] == self.template[8]:
            return True
        elif self.template[2] == self.template[5] and self.template[2] == self.template[8]:
            return True
        elif self.template[8] == self.template[7] and self.template[8] == self.template[6]:
            return True
        elif self.template[2] == self.template[4] and self.template[2] == self.template[6]:
            return True
        else:
            return False