#!/usr/bin/env python3
"""Sum of a list of floats and return the result."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.
    
    Args:
        input_list (List[float]): A list f float numbers.
        
    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
