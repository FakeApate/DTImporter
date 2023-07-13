class BaseClass:
    Type: str
    Properties: object

    def __new__(cls, doc: any):
        self = object.__new__(cls)
        self.Type = doc["Type"]
        self.__name__ = doc["Name"]
        self.Properties = doc["Properties"]
        return self
