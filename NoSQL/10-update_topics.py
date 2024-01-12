#!/usr/bin/env python3
"""sssss"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """dddddd"""

    mongo_collection.update({"name" : name}, {"$set" : {"topics" : topics}})
