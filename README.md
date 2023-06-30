# selenium-firefox1

Selenium4 を Windows上のFirefox とPython(v3.11)で試す。

## 準備

ドライバは親ディレクトリに置く。
[mozilla/geckodriver: WebDriver for Firefox](https://github.com/mozilla/geckodriver) の [release](https://github.com/mozilla/geckodriver/releases)から入手。

venvも親ディレクトリに置く。

```powershell
python -m venv ../.venv
../.venv/Scripts/Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```

## 実行1

```powershell
python ./test1.py
```

`tmp/mozilla.png` に [mozilla](https://www.mozilla.org/) のスクリーンショットが取られる。

## 参考

- [The Selenium Browser Automation Project | Selenium](https://www.selenium.dev/documentation/)
- [Firefox specific functionality | Selenium](https://www.selenium.dev/documentation/webdriver/browsers/firefox/)
- [mozilla/geckodriver: WebDriver for Firefox](https://github.com/mozilla/geckodriver)
- [Firefox/CommandLineOptions - MozillaWiki](https://wiki.mozilla.org/Firefox/CommandLineOptions#-private-window)

## メモ

Firefoxには「拡張機能(やaddon)を無効にする」起動オプションがないので、
あらかじめ空のプロファイルを作って、それを指定して([-Pオプション](https://wiki.mozilla.org/Firefox/CommandLineOptions#-P_.22profile_name.22))やるといいと思う。

FirefoxだとLinuxでも(Chromeと比べて少ない手間で)動くと思う、ので後で試す。
