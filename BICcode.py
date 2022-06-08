import re

class BICcode:

    def __init__(self, bic):
        self.bic=bic.upper()
        self.checksum=None
        self.ct={"A":"10",
                        "B":12,
                        "C":13,
                        "D":14,
                        "E":15,
                        "F":16,
                        "G":17,
                        "H":18,
                        "I":19,
                        "J":20,
                        "K":21,
                        "L":23,
                        "M":24,
                        "N":25,
                        "O":26,
                        "P":27,
                        "Q":28,
                        "R":29,
                        "S":30,
                        "T":31,
                        "U":32,
                        "V":34,
                        "W":35,
                        "X":36,
                        "Y":37,
                        "Z":38                            
                            } #div by 11 removed

            
    def calculate(self):
        if (self.bic_validate_string()):
            self.bic_seperate_checksum()
            ch=self.bic_return_checksum()
            if ch!=self.checksum and self.checksum!=None:
                print("given checksum is different from calculated checksum")
            return self.bic+str(ch)
            
    
    def bic_validate_string(self):
        if len(self.bic) not in (10, 11):
            print("Bic code needs to be 10 (without checksum) or 11 (with checksum)chars long.")
            return False
        if re.search("[A-Z]{4}[0-9]{6}", self.bic[:10])==None:
            print("Bic code not in valid form")
            return False
        if re.search("[A-Z]{3}[UJZ][0-9]{6}", self.bic[:10])==None:
            print("The 4th char needs to be U, J or Z")
            return False
        return True

    def bic_seperate_checksum(self):
        if len(self.bic)==11:
            self.bic=self.bic[0:10]
            self.checksum=self.bic[-1]
        else:
            self.checksum=None

            
    def bic_return_checksum(self):
        #step 1 map to number               
        y=[*[self.ct[e] for e in self.bic[:4]], *[int(e) for e in self.bic[4:]]]
        #multiple by order
        total=0
        for i in range(len(y)):
            total+=int(y[i])*(2**i)
        calc_checksum=total-(int(total/11)*11)
        return calc_checksum
            

#"MEDU7284869"
f=BICcode("MEAU200045")
print(f.calculate())


