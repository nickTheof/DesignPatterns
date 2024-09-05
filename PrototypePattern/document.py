from interface_prototype import IPrototype
import copy


class Document(IPrototype):
    "The Concrete Class"

    def __init__(self, name, l) -> None:
        self.name = name
        self.list = l

    def clone(self, mode):
        "Implement the clone abstract method using different copy techniques"

        if mode == 1:
            # results in a 1 level shallow copy of the Document
            doc_list = self.list
        if mode == 2:
            # results in a 2 level shallow copy of the Document
            doc_list = self.list.copy()
        if mode == 3:
            # recursive deep copy. Slower but results in a new copy
            # where no sub elements are shared by reference
            doc_list = copy.deepcopy(self.list)

        return type(self)(self.name, doc_list)

    def __str__(self) -> str:
        return f"{id(self)}\tname={self.name}\tlist={self.list}"
