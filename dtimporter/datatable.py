from .baseclass import BaseClass


class DataTable(BaseClass):
    Rows: dict

    def __new__(cls, doc: any):
        self = super(DataTable, cls).__new__(cls, doc)
        del self.Properties
        self.Rows = {}
        for k, v in (doc["Rows"]).items():
            self.Rows[k] = DataTableRow(v)
        del self.Type
        return self


class DataTableRow():
    def __init__(self, doc: dict):
        for k, v in doc.items():
            self[k] = v
        pass

    def __setitem__(self, key, value):
        setattr(self, key, value)
