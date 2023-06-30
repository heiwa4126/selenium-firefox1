#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Firefoxでselemiumのテスト。
大本: https://qiita.com/sszzszsz/items/4182c2b4aa4bf8f5037b
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from config import *

# オプションを準備
options = Options()
options.binary_location = FirefoxBinary
# options.add_argument("-headless")
# headありだと "Every renderer should have at least one task provided by a primary task provider." という警告が出る。
# headありだとデバッグに便利
# options.add_argument("--disable-extensions")  # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
options.add_argument("-private-window")  # シークレットモードで起動する
# オプションは https://wiki.mozilla.org/Firefox/CommandLineOptions 参照

# ドライバー指定でfirefoxブラウザを開く
service = Service(verbose=True, executable_path=FirefoxDriver)
driver = webdriver.Firefox(service=service, options=options)

# URLを開きスクショとる
driver.get("https://www.mozilla.org/")
driver.save_screenshot("tmp/mozilla.png")

driver.quit()
