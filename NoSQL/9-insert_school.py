#!/usr/bin/env python3
"""sssss"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """dddddd"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
