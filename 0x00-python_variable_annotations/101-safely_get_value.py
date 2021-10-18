#!/usr/bin/env python3
""" More involved type annotations """


from typing import Mapping, Any, TypeVar, Union


# The types of the elements of the input are not know
def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'),
                                    None] = None) -> Union[Any, TypeVar('T')]:
    """ More involved type annotations """
    if key in dct:
        return dct[key]
    else:
        return default
