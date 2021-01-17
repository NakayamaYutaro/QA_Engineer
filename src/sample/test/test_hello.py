#!/usr/bin/env python
# -*- coding: utf- -*-

import unittest
import test_main

class TestHello(unittest.TestCase):
  def test_greet(self):
    message = test_main.hello.greet()
    self.assertEqual(message, 'Hello,World!')
    #self.assertEqual(message, 'Hello, World!')

if __name__ == '__main__':
  unittest.main(verbosity=2)


