#!/usr/bin/env python3
"""oaaaa"""

import pymongo 


def list_all(mongo_collection):
    """ddddddd"""
    client = pymongo.MongoClient()
    return (client.mongo_collection.find())
    
if __name__ == '__main__':
    list_all(mongo_collection)
    