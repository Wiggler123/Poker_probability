class kort:
    #konstruktor
    def __init__(self,farg=None,varde=None): #Skapar kort där färg och värde ska skickas in
        self.farg = farg
        self.varde = varde

    #Destruktor
    def __del__(self):
        del self.varde
        del self.farg

    def view(self): #Visar kortets färg och värde
        print(self.farg + ' ' + str(self.varde))

    def get_farg(self): #här får vi tag på kortets färg
        return self.farg

    def get_varde(self): #Här får vi tag på kortets värde
        return self.varde

    def copy(self, kort): #Skapar en kopia av ett givet kort tex a= kort('Hjärter',5) a.copy('Spader',7)
        self.farg = kort.farg
        self.varde = kort.varde

    def compare(self,farg,varde): #Kollar om två kort är lika. Om de är returnera True annars False
        if self.farg == farg and self.varde == varde:
            return True
        else:
            return False