#!/usr/bin/env python3
"""sssss"""

import csv
import math
from typing import List
index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ddddddddd"""
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        lis = []
        if page * page_size > 19419:
            return lis
        doc = self.dataset()
        for i in range((page * page_size) - page_size,
                       (page * page_size) - 1):
            lis.append(doc[i])
        return lis

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """lokkkjujjjhh"""
        data = self.get_page(page, page_size)
        total_pages = 19419 // page_size
        prev_page = page - 1
        if page == 1:
            prev_page = None
        next_page = page + 1
        if page + 1 > total_pages:
            next_page = None
        return ({"page_size": page_size, "page": page,
                 "data": data, "next_page": next_page, "prev_page": prev_page,
                 "total_pages": total_pages})
