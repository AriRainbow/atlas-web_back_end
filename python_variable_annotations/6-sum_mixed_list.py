#!/usr/bin/env python3
"""Sum a list containing both ints and floats, and return the result."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list with both integers anf floats.
    
    Returns:
        float: The total sum of all elements in the list, as a float.
    """
    return sum(mxd_lst)
