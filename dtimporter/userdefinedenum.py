from .baseclass import BaseClass
class Enum(BaseClass):
    def __new__(cls, doc: any):

        self = super(Enum, cls).__new__(cls, doc)
        displaymap = self.Properties.get("DisplayNameMap")
        for item in displaymap:
            name = list(item)[0]
            d: dict = item[name]
            r = d.get("CultureInvariantString")
            if r is not None:
                self[name] = r
            else:
                raise ValueError
        del self.Properties
        del self.Type
        return self

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)