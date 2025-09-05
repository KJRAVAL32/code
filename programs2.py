class product:
    def __init__(self,name,code,categeoy,price):
        self.name = name
        self.code = int(code)
        self.categeoy = categeoy
        self.price = int(price)
class Category:
    def __init__(self,name,code,parent=None):
        self.name=name
        self.code = code
        self.parent=parent
        self.display_name=self._get_display_name()

    def _get_display_name(self):
        if self.parent:
            return self.parent,">",self.name
        else:
            return self.name
c1=Category("vehicle",1)
c2=Category("car",2,c1)
c3=Category("disel",3,c2)
c4=Category("power",4,c3)
c1._get_display_name()
c2._get_display_name()
c3._get_display_name()
c4._get_display_name()