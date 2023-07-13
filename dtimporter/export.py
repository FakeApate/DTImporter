import os
import re
import jsonpickle
import dtimporter

importedEnums = {}
importedDataTables = {}
pattern = re.compile("^(E|DT)_[a-zA-Z]*[a-zA-Z_]*.json$")

database = [os.path.join(root, name)
            for root, dirs, files in os.walk("data/Export/Medieval_Dynasty/Content/Blueprints")
            for name in files
            if pattern.match(name)]

for file in database:
    dynobj = dtimporter.create(file)
    if dynobj is None:
        continue
    if dynobj.__name__.startswith("E_"):
        importedEnums[dynobj.__name__] = dynobj
    elif dynobj.__name__.startswith("DT_"):
        importedDataTables[dynobj.__name__] = dynobj

dtimporter.reviveReferences(importedDataTables, importedEnums)

encoded = jsonpickle.encode(importedDataTables)
with open("convertedDB.json", encoding='utf-8', mode="w") as json_data:
    json_data.write(encoded)
    json_data.close()
