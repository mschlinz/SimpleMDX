


class member:

    def __init__(self, dimension: str, element: str, hierarchy: str = '') -> None:

        self.dimension = mdx_format(dimension)
        self.element = mdx_format(element)
        self.hierarchy = mdx_format(hierarchy) if hierarchy else self.dimension

    def to_mdx(self) -> str:
        return "[" + self.dimension + "].[" + self.hierarchy + "].[" + self.element + "]"


def mdx_format(value: str) -> str:
    '''
    formatting string to be in uppercase and no spaces

    Args:
        value (str): string that needs to be adjusted

    Returns:
        str: formatted string
    '''
    return value.upper().replace(' ', '')