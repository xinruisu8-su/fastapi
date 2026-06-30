# FastAPI

1.安装
打开终端，输入
```shell
$ pip install fastapi 
```

2.写app/main.py
```python
from fastapi import FastAPI

app = FastAPI() #创建了一个FastAPI类的对象，对象放入app变量中

@app.get("/")
def home():
    return {"message":"Hello FastAPI"}
```

3.