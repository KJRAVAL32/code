class product:
    def __init__(self,name,code,categeoy,price):
        self.name = name
        self.code = int(code)
        self.categeoy = categeoy
        self.price = int(price)
class Category:
    def __init__(self,name,code,parent=''):
        self.name=name
        self.code = code
        self.parent=parent
        self.display_name=self._get_display_name()

    def _get_display_name(self, child_name=None):
        # if self.parent and child_name != '':
            if self.parent:
                # child_name = self.parent.name
                return f"{self.parent.name}>{self.name}"
            else:
                return self.name
        # elif self.parent and child_name == '':
        #     if self.parent.parent:
        #         child_name = self.parent.name
        #         return f"{self.parent._get_display_name(child_name)} > {self.parent.name} > {self.name}"
c1=Category("vehicle",1)
c2=Category("car",2,c1)
c3=Category("disel",2,c2)
# print(c1.display_name)
print(c3.display_name)
