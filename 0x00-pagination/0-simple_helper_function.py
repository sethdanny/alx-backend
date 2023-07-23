#!/usr/bin/env python3
"""introduction to pagination"""


def index_range(page, page_size):
    """function which retrieves the content on pages"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
