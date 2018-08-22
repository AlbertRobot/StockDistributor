# -*- coding: utf-8 -*-
import configparser

config = configparser.ConfigParser()


def conf_redis(conf_file):
    default_conf = {'host': 'localhost', 'port': '6379', 'db': 0}
    section_redis = 'redis'
    config.read(conf_file)
    if section_redis in config:
        default_conf['host'] = config[section_redis]['host']
        default_conf['port'] = config[section_redis]['port']
        default_conf['db'] = config[section_redis]['db']
    return default_conf
