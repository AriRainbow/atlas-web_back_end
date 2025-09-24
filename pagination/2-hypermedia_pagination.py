#!/usr/bin/env python3
"""
This module provides a Server class with hypermedia pagination
support for a dataset of popular baby names.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of (start_index, end_index) for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and end index (exclusive) of the items for the requested page.
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
  
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns pagination metadata with the page data.

        Args:
            page (int): Current page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            Dict[str, Any]: Pagination metadata including:
                - page_size: size of the returned page
                - page: current page number
                - data: the actual page of the dataset
                - next_page: number of the next page or None
                - prev_page: number of the previous page or None
                - total_pages: total number of pages
        """
        data = self.get_page(page, page_size)
        dataset_len = len(self.dataset())
        total_pages = math.ceil(dataset_len / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
