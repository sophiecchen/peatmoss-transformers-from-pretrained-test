#!/usr/bin/python
# -*- coding: utf-8 -*-

# run with pytest

import unittest
from peatmoss_transformers_test import head

class Test(unittest.TestCase):
    def test_main(self):
        self.assertEqual(side.pure_import(), 0)

if __name__ == '__main__':
    unittest.main()