# -*- coding: utf-8 -*-

from distributor import client


CHAN = '600340'  # redis KEY
if __name__ == '__main__':
    """
    行情订阅者
    """
    ps = client.subscribe(CHAN)
    print('ready to subscribe channel: ' + CHAN)
    for item in ps.listen():
        if item['type'] == 'message':
            coming = eval(str(item['data'], encoding="utf-8"))
            print(coming)
