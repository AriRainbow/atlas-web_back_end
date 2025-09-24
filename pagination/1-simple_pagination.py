#!/usr/bin/env python3
"""
This module provides a Server class to paginate a dataset
of popular baby names stored in a CSV file.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of (start_index, end_index) for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and the end index (exclusive) of the items for the requested page.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches dataset from CSV file.

        Returns:
            List[List]: The cached dataset excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset
  
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page from the dataset.

        Args:
            page (int): The page number to return (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows from the dataset for the requested page.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start:end]
