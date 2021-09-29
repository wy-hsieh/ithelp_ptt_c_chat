# 載入 requests 套件
import requests
# 載入 BeautifulSoup 套件
from bs4 import BeautifulSoup

# 取得 c_chat 文章列
response = requests.get("https://www.ptt.cc/bbs/C_Chat/index.html")
root = BeautifulSoup(response.text, "html.parser")

# 取得文章標題
titles = root.find_all("div", class_ = "title")
for title in titles:
  print(title.text.strip())