# -*- coding: utf-8 -*-
# Unit Test # 1

import hashlib
from md5 import calc_md5

#以下の実装だとmd5 calc_md5と同じ実装内容となるのでNG
def test_calc_md5():
  actual = calc_md5(" This is Content ")
  m = hashlib.md5()
  m.update(b"This is Content")
  assert actual == m.hexdigest()


def test_correct_calc_md5():
  actual = calc_md5(" This is Content ")
  assert actual == b"e61994e96b20e3965b61de16077e18c7", '期待値：{0}'.format(actual)

test_correct_calc_md5()  
