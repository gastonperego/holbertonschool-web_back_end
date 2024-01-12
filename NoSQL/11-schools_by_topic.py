#!/usr/bin/env python3
"""sssss"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """flllllllll"""
    lis = []
    for school in mongo_collection.find().items():
        if topic in school["topics"]:
            lis.append(school["name"])
    return lis