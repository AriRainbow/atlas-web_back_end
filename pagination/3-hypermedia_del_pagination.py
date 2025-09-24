#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by original sorting position, starting at 0.

        Returns:
            Dict[int, List]: Dictionary of index-to-row mappings.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a page of the dataset starting from a given index,
        resilient to deletions.

        Args:
            index (int): The starting index of the page.
            page_size (int): Number of items in the page.

        Returns:
            Dict[str, Any]: A dictionary with pagination info:
                - index: the current start index of the return page
                - next_index: index to start the next page
                - page_size: the number of items returned
                - data: list of actual dataset rows
        """
        assert isinstance(index, int) and index >= 0, "Index must be a non-negative integer"

        indexed_data = self.indexed_dataset()
        assert index < len(self.dataset()), "Index out of range"

        data: List[List] = []
        current_index = index
        collected = 0

        while collected < page_size and current_index < len(self.dataset()):
            item = indexed_data.get(current_index)
            if item:
                data.append(item)
                collected += 1
            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data
        }
