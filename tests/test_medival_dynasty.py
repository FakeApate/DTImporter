import os
import re
import unittest
import jsonpickle
import dtimporter


class BasicRuntimeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        global importedEnums
        global importedDataTables
        importedEnums = {}
        importedDataTables = {}
        return super().setUpClass()
   

    def test_All(self):
        pattern = re.compile("^(E|DT)_[a-zA-Z]*[a-zA-Z_]*.json$")
        database = [os.path.join(root, name)
                    for root, dirs, files in os.walk("data/")
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
            else:
                self.fail(
                    "Dynamic Object Name starts neither with 'E_' or 'DT_'")

        dtimporter.reviveReferences(
            importedDataTables, importedEnums)

        encoded = jsonpickle.encode(importedDataTables)
        with open("convertedDB.json", encoding='utf-8', mode="w") as json_data:
            json_data.write(encoded)
            json_data.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:

        os.remove("convertedDB.json")
        del importedDataTables
        del importedEnums
        return super().tearDownClass()

if __name__ == '__main__':
    unittest.main()
