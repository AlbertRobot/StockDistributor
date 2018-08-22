# -*- coding: utf-8 -*-
import datetime
import sys
import time

from distributor import client
from distributor import collector, conf
import schedule

CHAN = '600340'  # redis KEY
INTERVAL = 3  # seconds
DATA_FILE = sys.path[0] + '/conf/testdata.csv'
CONFIG_FILE = sys.path[0] + '/conf/app.conf'


def job():
    """
    pub 任务
    获取距当前时间最近时间的行情
    """
    now = datetime.datetime.now()
    print('pub job start at ' + now.strftime('%Y-%m-%d %H:%M:%S'))
    val = collector.collect(now.strftime('%H%M%S'), DATA_FILE)
    client.publish(CHAN, val)
    print('pub end')


if __name__ == '__main__':
    # 定时调度任务
    conf.conf_redis()
    schedule.every(INTERVAL).seconds.do(job).run()
    while True:
        schedule.run_pending()
        time.sleep(1)
