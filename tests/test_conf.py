# -*- coding: utf-8 -*-
import unittest
from distributor import conf


class CollectorTest(unittest.TestCase):

    def test_collect(self):
        config = conf.conf_redis('testapp.conf')
        self.assertEqual(config['port'], '6380')


if __name__ == '__main__':
    unittest.main()
