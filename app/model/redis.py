# coding=utf-8
# Author: gdream@126.com
from redis import Redis, ConnectionPool


class RedisClient:
    def __init__(self, config):
        pool = ConnectionPool(host=config[0],
                              port=config[1],
                              db=config[2],
                              password=config[3],
                              max_connections=config[5])
        self.client = Redis(connection_pool=pool, decode_responses=True)

    def set(self, key, value):
        self.client.set(key, value)

    def get(self, key):
        self.client.get(key).decode()
