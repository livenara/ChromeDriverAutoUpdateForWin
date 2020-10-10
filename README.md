# 使い方

Seleniumで使う
Windows用のChromeDriverの自動更新コード

ブラウザが起動しなければドライバーの更新をかけます。

## バージョン

Python 3.7で作成

### 必要なモジュール

chromedriver-binary

```
$ pip install chromedriver-binary
```

### コード

```
from selenium import webdriver
import chromedriver_binary
import ChromeDriverUpdate

try:
    driver = webdriver.Chrome()
except:
    ChromeDriverUpdate.chromeDriverUpdate()
    driver = webdriver.Chrome()

driver.get("https://yahoo.co.jp")
```