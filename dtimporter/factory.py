import json
import re
from .datatable import DataTable, DataTableRow
from .baseclass import BaseClass
from .userdefinedenum import Enum


def create(path: str) -> object():
    with open(path, encoding='utf-8') as json_data:
        cleantext = re.sub("_[0-9]+_[a-fA-F0-9]{32}", '', json_data.read())
        data = json.loads(cleantext)
    if len(data) != 1:
        raise TypeError("Data should be a list with single entry")
    base = BaseClass(data[0])
    if base.Type == "UserDefinedEnum":
        try:
            dynObj = Enum(data[0])
        except ValueError:
            return None
    elif base.Type == "DataTable":
        dynObj = DataTable(data[0])
    else:
        raise TypeError("Json object has no valid type")
    del base
    return dynObj


def checkType(obj: any, enums: dict[str, object], parent: any, varname="None"):
    if type(obj) is list:
        itList(obj, enums)
    elif type(obj) is dict:
        itDict(obj, enums)
    elif type(obj) is str:
        itValue(obj, enums, parent, varname)
    pass


def itList(obj: list, enums: dict[str, object]):
    for i in obj:
        checkType(i, enums, obj)
    pass


def itDict(obj: dict, enums: dict[str, object]):
    for k, v in obj.items():
        checkType(v, enums, obj, k)
    pass


def itValue(obj: str, enums: dict[str, object], parent: any, varname: str):
    if obj.startswith("E_"):
        [enumName, value] = obj.split("::")
        enum = enums.get(enumName)
        if enum is None:
            raise ValueError("Enum Name is not in known enum list")
        if type(parent) is dict or type(parent) is DataTableRow:
            parent[varname] = enum[value]
    pass


def reviveReferences(tables: dict[str, object], enums: dict[str, object]):
    for kTable, vTable in tables.items():
        for kRow, vRow in vTable.Rows.items():
            for kItem, vItem in vRow.__dict__.items():
                checkType(vItem, enums, kRow, kItem)
    pass
