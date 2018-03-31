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
                               
keyPool = {'体育': ['NBA', '英超', '电竞'], 'python': ['pytorch','pyspark']}
for data in news.generate(keyPool=keyPool,pymysql_conn=conn,tableName='t_news'):
    print(data)

# run, see luck in your database!
```


- *Tips:*
```python
generate(keyPool=None,outTitle=None,outContent=None,minLength=200,perKeyNum=20,sentimentApi=None,
        pymysql_conn=None,tableName='News')
```
