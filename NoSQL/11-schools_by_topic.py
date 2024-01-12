#!/usr/bin/env python3
"""sssss"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """flllllllll"""
    return list(mongo_collection.find({"topics": topic}))