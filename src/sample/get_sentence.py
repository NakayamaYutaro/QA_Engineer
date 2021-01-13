# -*- coding: utf-8 -*-

from selenium import webdriver
from pandas import *
import time

# PhantomJS経由でウェブページを取得する
browser = webdriver.PhantomJS()
url = "http://b.hatena.ne.jp/search/text?safe=on&q=Python&users=50"
browser.get(url)
df = pandas.read_csv('trend.csv', index_col=0)

while True:
  #CSSセレクタ(クラスセレクタ)を指定して、pager番号が0以上の場合は処理を行う
  if len(browser.find_elements_by_css_selector(".pager-next")) > 0:
    print("######################page: {} ########################".format(page))
    print("Starting to get posts...")
    #ページ内のすべてのポスト情報を取得
    posts = browser.find_elements_by_css_selector(".search-result")
    
    for post in posts:
      title = post.find_element_by_css_selector("h3").text
      date = post.find_element_by_css_selector(".created").text
      bookmarks = post.find_element_by_css_selector(".users span").text
      se = pandas.Series([title, date, bookmarks],['title','date','bookmarks'])
      df = df.append(se, ignore_index=True)
      print(df)

    btn = browser.find_element_by_css_selector("a.pager-next").get_attribute("href")
    print("next url:{}".format(btn))
    browser.get(btn)
    page+=1
    browser.implicitly_wait(10)
    print("Moving to next page......")
    time.sleep(10)
  else: #if no pager exist, stop.
    print("no pager exist anymore")
    break
df.to_csv("trend1.csv")
print("DONE")
