#!/usr/bin/env python3
"""sssss"""

import pymongo


if __name__ == "__main__":
    """oaaaaa"""
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx
    num_of_docs = nginx.count_documents({})
    print(f"{num_of_docs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        num_of_method = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {num_of_method}")
    status = nginx.count_documents({"method": "GET","path": "/status"})
    print(f"{status} status check")
