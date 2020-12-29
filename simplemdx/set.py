from simplemdx.member import member
from typing import List, Union

class set:

    def __init__(self, dimension: str, hierarchy: str = ''):

        self.dimension = dimension
        self.hierarchy = hierarchy if hierarchy else self.dimension

    
    def member(self, element: str) -> set:

        class MemberClass(set):
            def __init__(self, dimension: str, element: str, hierarchy: str = ''):
                self.mem = member(self.dimension, element, self.hierarchy)

            def to_mdx(self, indent: int = 0):
                return "{" + self.mem.to_mdx() + "}"

        return MemberClass(self.dimension, element, self.hierarchy)
                
    def members(self, elements: List[str]) -> set:

        class MembersClass(set):
            def __init__(self, dimension: str, elements: List[str], hierarchy: str = ''):
                self.mems = [
                    member(dimension, el, hierarchy).to_mdx()
                    for el in elements
                ]
            
            def to_mdx(self, indent: int = 0):
                inner_indent, outer_indent = get_indentation(indent)
                mdx_mems = [self.mems[0]]
                mdx_mems.extend(
                    [
                        ',' + m 
                        for m in self.mems[1:]
                    ]
                )
                
                mdx_mems = ''.join([
                    inner_indent + m 
                    for m in mdx_mems
                ])

                return "{" + mdx_mems + outer_indent + "}"

        

        return MembersClass(self.dimension, elements, self.hierarchy)

def get_indentation(indent: Union[bool, int] ):

    if (type(indent) == bool) and indent:
        indent = 0
    else:
        return '', ''

    indentation = ['\n']

    indentation.extend(['\t'] * indent)
    outer = ''.join(indentation)

    indentation.append('\t')
    inner = ''.join(indentation)

    return inner, outer
