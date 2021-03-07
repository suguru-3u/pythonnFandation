# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# ブラウザを開く。
driver = webdriver.Chrome(executable_path='/Users/oohirasuguru/Downloads/chromedriver')
# Googleの検索TOP画面を開く。
driver.get("https://www.google.co.jp/")
print('A')
# 検索語として「selenium」と入力し、Enterキーを押す。
driver.find_element_by_name("q").send_keys("Twitter")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
# driver.find_element_by_link_text("twitter.com").click()
print('B')  
# 5秒間待機してみる。
sleep(5)
# ブラウザを終了する。
driver.close()