from simplemdx.member import member
from typing import List

class set:

    def __init__(self, dimension: str, hierarchy: str = ''):

        self.dimension = dimension
        self.hierarchy = hierarchy if hierarchy else self.dimension

    
    def member(self, element: str) -> set:

        class MemberClass(set):
            def __init__(self, dimension: str, element: str, hierarchy: str = ''):
                self.mem = member(self.dimension, element, self.hierarchy)

            def to_mdx(self):
                return "{" + self.mem.to_mdx() + "}"

        return MemberClass(self.dimension, element, self.hierarchy)
                
    def members(self, elements: List[str]) -> set:

        class MembersClass(set):
            def __init__(self, dimension: str, elements: List[str], hierarchy: str = ''):
                self.mems = [
                    member(dimension, el, hierarchy).to_mdx()
                    for el in elements
                ]
            
            def to_mdx(self):
                return "{" + ''.join(self.mems) + "}"

        return MembersClass(self.dimension, elements, self.hierarchy)