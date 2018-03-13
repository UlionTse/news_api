## ***The document of [news_api]()*** ##


- *Usage:*

```python
from news_api import news

for data in news.generate():
    print(data)

```

- *Tips:*
```python
generate(keyPool=None,outTitle=None,outContent=None,minLength=200,perKeyNum=20,sentimentApi=None,
        pymysql_conn=None,tableName='News')
```
