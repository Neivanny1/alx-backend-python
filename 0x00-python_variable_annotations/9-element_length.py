#!/usr/bin/env python3
'''
 Let's duck type an iterable object
'''


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Outputs list of tuples, one for each element, of which
    consists of the element itself and its length.
    '''
    return [(i, len(i)) for i in lst]
