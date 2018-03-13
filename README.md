## ***The document of [news_api]()*** ##


- *Usage:*

```python
from news_api import news

for data in news.generate():
    print(data)

```


```python
import pymysql
from news_api import news

conn = pymysql.connect(host='xxx.xx.xx.xx',
                       port=3306,
                       user='xxxx',
                       password='xxxx',
                       database='xxxx',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
                               
keyPool = {'新闻': ['科技', '财经', '体育']}
news.generate(keyPool=keyPool,pymysql_conn=conn,tableName='t_news')

# run, see luck in your database!
```


- *Tips:*
```python
generate(keyPool=None,outTitle=None,outContent=None,minLength=200,perKeyNum=20,sentimentApi=None,
        pymysql_conn=None,tableName='News')
```
