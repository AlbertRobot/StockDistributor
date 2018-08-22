# -*- coding: utf-8 -*-

import unittest
from distributor import client


class ClientTest(unittest.TestCase):

    @classmethod
    def test_publish(self):
        client.publish('test', 'val')

    @classmethod
    def test_subscribe(self):
        client.subscribe('test')


if __name__ == '__main__':
    unittest.main()
