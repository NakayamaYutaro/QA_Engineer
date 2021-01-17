# -*- coding: utf-8 -*-
#ユニットテスト演習
#テストにテスト対象と同等実装を書かないこと
import hashlib

def calc_md5(content):
  content = content.strip()
  m = hashlib.md5()
  m.update(content.encode('utf-8'))
  return m.hexdigest()
