class kort:
    def __init__(self,farg=None,varde=None):
        self.farg = farg
        self.varde = varde

    def __del__(self):
        del self.varde
        del self.farg

    def view(self):
        print(self.farg + ' ' + str(self.varde))

    def get_farg(self):
        return self.farg

    def get_varde(self):
        return self.varde

    def copy(self, kort):
        self.farg = kort.farg
        self.varde = kort.varde

    def compare(self,farg,varde):
        if self.farg == farg and self.varde == varde:
            return True
        else:
            return False
