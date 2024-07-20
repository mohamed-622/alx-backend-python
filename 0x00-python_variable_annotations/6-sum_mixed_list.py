#!/usr/bin/env python3
""" Module for the function sum_mixed_list """

from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float.
    """
    return sum(input_list)
