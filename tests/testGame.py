#! /usr/bin/env python
#
#

import sys
import os
sys.path.append(os.environ['PythonScriptRoot'])
import EnvPython
import logging
from Utilities import *
import unittest

class TestGame(TestCaseEnv):
    @classmethod
    def setUpClass(cls):
        TestCaseEnv.setUpClass()


    @classmethod
    def tearDownClass(cls):
        TestCaseEnv.tearDownClass()

    def setUp(self):
        TestCaseEnv.setUp(self)


    def tearDown(self):
        pass

	def test1(self):
		pass

if __name__ == '__main__':
	unittest.main()


