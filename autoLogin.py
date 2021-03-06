import sys
import sys
from selenium import webdriver
import os
os.chdir("c:\\your-execpath\\login_sample")
import logging
import logging.config
# ログ出力設定　※本件では詳細割愛
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')
logging.debug("AUTO LOGIN START")
# 自動ログイン関数を宣言
#
#