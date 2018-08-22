# -*- coding: utf-8 -*-
import datetime
import unittest
from distributor import collector


class CollectorTest(unittest.TestCase):

    def test_collect(self):
        now = datetime.datetime.now()
        val = collector.collect(now.strftime('%H%M%S'), 'testdata.csv')
        self.assertIsNotNone(val)


if __name__ == '__main__':
    unittest.main()
