#!/usr/bin/env python3
"""This module defines a function that returns the length of each sequence in an iterable."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-like objects (strings, lists, tuples).
    
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each contains an element from the iterable
                                    and the length of that element.
    """
    return [(i, len(i)) for i in lst]
