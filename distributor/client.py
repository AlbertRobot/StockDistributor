# -*- coding: utf-8 -*-

import redis
from distributor import conf

# redisClient 初始化
config = conf.conf_redis('../conf/app.conf')
rClient = redis.StrictRedis(host=config['host'], port=config['port'], db=config['db'])


def publish(key, val):
    """
    数据发布
    :param key: 发布KEY
    :param val: 发布Value
    """
    rClient.publish(key, val)


def subscribe(key):
    """
    redis消息订阅
    :param key: 订阅CHAN
    :return: Publish/Subscribe object
    """
    ps = rClient.pubsub()
    ps.subscribe(key)
    return ps
