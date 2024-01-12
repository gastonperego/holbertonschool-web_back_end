#!/usr/bin/env python3
"""oaaaa"""

import pymongo 


def list_all(mongo_collection):
    """ddddddd"""
    lis = []
    for doc in mongo_collection.find():
        lis.append(doc)
    return lis

if __name__ == '__main__':
    list_all(mongo_collection)
    