# -*- coding: utf-8 -*-

import pandas as pd


def collect(recent_time, data_file):
    """
    获取最新行情数据
    :param recent_time: 当前时间
    :param data_file: 数据文件
    :return: dict
    """
    df = pd.read_csv(data_file, sep='\t')
    df = df[(df['time'] <= int(recent_time))][['price/last', 'price/sell1']]
    if df is not None:
        return df.tail(1).to_dict(orient='list')
    else:
        return ''  # 未找到数据
