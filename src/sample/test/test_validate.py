# -*- coding: utf-8 -*-
import test_main as tm

def test_valid():
  """検証が正しい場合"""
  assert tm.validate_func("a")
  assert tm.validate_func("a" * 50)
  assert tm.validate("a" * 100)
  assert tm.validate("")
  assert tm.validate("a" * 101)
